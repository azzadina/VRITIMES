import React, {useLayoutEffect, useRef, useState, useEffect} from 'react';
import {AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, useVideoConfig, delayRender, continueRender} from 'remotion';
// Same drawing code as the VRITIMES SNS Dashboard preview
// eslint-disable-next-line @typescript-eslint/no-var-requires
const Scene = require('./scene.js');

// Fonts ship inside the project (public/fonts) so rendering needs no font download.
const FONT_FILES: string[][] = [["VRPoppins","400","fonts/VRPoppins-400.woff"],["VRPoppins","600","fonts/VRPoppins-600.woff"],["VRPoppins","700","fonts/VRPoppins-700.woff"],["VRPoppins","800","fonts/VRPoppins-800.woff"],["VRInter","400","fonts/VRInter-400.woff"],["VRInter","500","fonts/VRInter-500.woff"],["VRInter","600","fonts/VRInter-600.woff"],["VRInter","700","fonts/VRInter-700.woff"],["VRCaveat","700","fonts/VRCaveat-700.woff"]];
let fontsPromise: Promise<unknown> | null = null;
const loadFonts = () => {
  if (!fontsPromise) fontsPromise = Promise.all(FONT_FILES.map(([family, weight, file]) => {
    const ff = new FontFace(family, 'url(' + staticFile(file) + ')', {weight});
    return ff.load().then((f) => { (document as any).fonts.add(f); }).catch(() => null);
  }));
  return fontsPromise;
};

type Props = {reel: any; durs: number[]; hasVo: boolean};

export const reelMetadata = async () => {
  const reel = await fetch(staticFile('reel.json')).then((r) => r.json());
  let timing: any = null;
  try { const r = await fetch(staticFile('vo/timing.json')); if (r.ok) timing = await r.json(); } catch (e) { timing = null; }
  const est = Scene.timeline(reel).durs;
  const durs = reel.scenes.map((s: any, i: number) => {
    const vo = timing && timing[i] && timing[i].duration ? timing[i].duration + 0.45 : 0;
    return Math.max(1.6, vo || est[i]);
  });
  const total = durs.reduce((a: number, b: number) => a + b, 0);
  return {durationInFrames: Math.ceil(total * 30), props: {reel, durs, hasVo: !!timing}};
};

export const Reel: React.FC<Props> = ({reel, durs, hasVo}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const ref = useRef<HTMLCanvasElement>(null);
  const [assets, setAssets] = useState<any>(null);
  const [handle] = useState(() => delayRender('Loading logos, icons and fonts'));
  useEffect(() => {
    Promise.all([
      Scene.loadAssets({logoWhite: staticFile('logo/stack_white.png'), logoColor: staticFile('logo/stack_color.png'), besideWhite: staticFile('logo/beside_white.png')}),
      loadFonts(),
    ]).then(([a]) => { setAssets(a); continueRender(handle); });
  }, [handle]);
  useLayoutEffect(() => {
    if (!assets || !ref.current || !reel) return;
    const ctx = ref.current.getContext('2d');
    Scene.drawFrame(ctx, reel, durs, frame / fps, assets, {
      fHead: 'VRPoppins', fBody: 'VRInter', fHand: 'VRCaveat',
      lang: reel.lang, cc: reel.country, countryName: reel.countryName, roleTitle: reel.roleTitle || 'PR Specialist',
    });
  }, [frame, assets, reel, durs, fps]);
  let acc = 0;
  return (
    <AbsoluteFill style={{backgroundColor: '#E9EFF9'}}>
      <canvas ref={ref} width={1080} height={1920} style={{width: '100%', height: '100%'}} />
      {reel && reel.sfx !== false && Scene.sfxCues(reel, durs).map((c: any, k: number) => (
        <Sequence key={'sfx' + k} from={Math.round(c.t * fps)} durationInFrames={Math.round(1.2 * fps)}>
          <Audio src={staticFile('sfx/' + c.name + '.wav')} volume={c.vol * (reel.sfxVolume == null ? 1 : reel.sfxVolume)} />
        </Sequence>
      ))}
      {hasVo && reel && reel.scenes.map((s: any, i: number) => {
        const from = Math.round(acc * fps); acc += durs[i];
        if (!String(s.vo || '').trim()) return null;
        return (
          <Sequence key={i} from={from} durationInFrames={Math.max(1, Math.round(durs[i] * fps))}>
            <Audio src={staticFile('vo/s' + String(i + 1).padStart(2, '0') + '.mp3')} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
