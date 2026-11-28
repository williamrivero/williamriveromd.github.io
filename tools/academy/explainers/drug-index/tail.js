function bg(i, T) {
  var g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, ['#eef7f6', '#f8f5ee', '#f3f6fb', '#f3f7f2', '#f4f2fa', '#f8f5ee', '#eef7f6', '#eef7f6'][i]); g.addColorStop(1, '#ffffff');
  x.fillStyle = g; x.fillRect(0, 0, W, H);
  x.fillStyle = 'rgba(26,107,114,.06)'; for (var k = 0; k < 6; k++) { x.beginPath(); x.arc(1120 - k * 40 + Math.sin(T * .3 + k) * 10, 80 + k * 22, 60 + k * 18, 0, Math.PI * 2); x.fill(); }
  x.fillStyle = 'rgba(31,56,100,.05)'; x.fillRect(0, 640, W, 80);
}

window.render = function (frame) {
  var fps = TL.fps, T = frame / fps, i = 0, start = 0;
  while (i < TL.scenes.length - 1 && frame >= start + TL.scenes[i].frames) { start += TL.scenes[i].frames; i++; }
  var sc = TL.scenes[i], lt = (frame - start) / fps;
  bg(i, T);
  scenes[i](lt, T);
  // the content fades between scenes; the guide stays
  var d = sc.frames / fps, f = Math.max(0, 1 - lt / .3, 1 - (d - lt) / .3);
  if (f > 0) { x.save(); x.globalAlpha = f; bg(i, T); x.restore(); }
  guide(T, TL.amp[frame] || 0, i === 0 && lt < 3.5 ? 'wave' : 'point', lt);
  caption(sc, lt);
  if (frame < 12) { x.fillStyle = 'rgba(255,255,255,' + (1 - frame / 12) + ')'; x.fillRect(0, 0, W, H); }
};
</script></body></html>
