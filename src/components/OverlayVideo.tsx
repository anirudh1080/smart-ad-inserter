import React from 'react';
import { Video, Img, AbsoluteFill } from 'remotion';

type OverlayVideoProps = {
  videoSrc: string;
  adGifSrc: string;
  qrCodeSrc: string;
};

export const OverlayVideo: React.FC<OverlayVideoProps> = ({ videoSrc, adGifSrc, qrCodeSrc }) => {
  return (
    <AbsoluteFill style={{ backgroundColor: 'black' }}>
      <Video
        src={videoSrc}
        startFrom={0}
        volume={1}
        style={{
          objectFit: 'cover',
          width: '100%',
          height: '100%',
        }}
      />
      
      {/* L-band at the top */}
      <AbsoluteFill style={{ top: '0', left: '0', width: '100%', height: '15%' }}>
        <div
          style={{
            backgroundColor: 'rgba(0, 0, 0, 0.7)',
            color: 'white',
            padding: '10px',
            fontSize: '24px',
            textAlign: 'center',
          }}
        >
          L-Band Content Here
        </div>
      </AbsoluteFill>

      {/* Advertisement GIF on the left */}
      <AbsoluteFill style={{ top: '0', left: '0', width: '20%', height: '100%' }}>
        <Img
          src={adGifSrc}
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
          }}
        />
      </AbsoluteFill>

      {/* QR code below the L-band */}
      <AbsoluteFill style={{ bottom: '5%', left: '50%', transform: 'translateX(-50%)', width: '10%' }}>
        <Img
          src={qrCodeSrc}
          style={{
            width: '100%',
            height: 'auto',
            objectFit: 'contain',
          }}
        />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
