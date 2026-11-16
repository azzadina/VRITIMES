import React from 'react';
import {Composition} from 'remotion';
import {Reel, reelMetadata} from './Reel';

export const RemotionRoot: React.FC = () => (
  <Composition
    id="VritimesReel"
    component={Reel as any}
    width={1080}
    height={1920}
    fps={30}
    durationInFrames={30 * 30}
    defaultProps={{reel: null, durs: [], hasVo: false}}
    calculateMetadata={reelMetadata as any}
  />
);
