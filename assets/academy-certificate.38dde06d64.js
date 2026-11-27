//---------------------------------------------------------------------
//
// QR Code Generator for JavaScript
//
// Copyright (c) 2009 Kazuhiko Arase
//
// URL: http://www.d-project.com/
//
// Licensed under the MIT license:
//  http://www.opensource.org/licenses/mit-license.php
//
// The word 'QR Code' is registered trademark of
// DENSO WAVE INCORPORATED
//  http://www.denso-wave.com/qrcode/faqpatent-e.html
//
//---------------------------------------------------------------------

var qrcode = function() {

  //---------------------------------------------------------------------
  // qrcode
  //---------------------------------------------------------------------

  /**
   * qrcode
   * @param typeNumber 1 to 40
   * @param errorCorrectionLevel 'L','M','Q','H'
   */
  var qrcode = function(typeNumber, errorCorrectionLevel) {

    var PAD0 = 0xEC;
    var PAD1 = 0x11;

    var _typeNumber = typeNumber;
    var _errorCorrectionLevel = QRErrorCorrectionLevel[errorCorrectionLevel];
    var _modules = null;
    var _moduleCount = 0;
    var _dataCache = null;
    var _dataList = [];

    var _this = {};

    var makeImpl = function(test, maskPattern) {

      _moduleCount = _typeNumber * 4 + 17;
      _modules = function(moduleCount) {
        var modules = new Array(moduleCount);
        for (var row = 0; row < moduleCount; row += 1) {
          modules[row] = new Array(moduleCount);
          for (var col = 0; col < moduleCount; col += 1) {
            modules[row][col] = null;
          }
        }
        return modules;
      }(_moduleCount);

      setupPositionProbePattern(0, 0);
      setupPositionProbePattern(_moduleCount - 7, 0);
      setupPositionProbePattern(0, _moduleCount - 7);
      setupPositionAdjustPattern();
      setupTimingPattern();
      setupTypeInfo(test, maskPattern);

      if (_typeNumber >= 7) {
        setupTypeNumber(test);
      }

      if (_dataCache == null) {
        _dataCache = createData(_typeNumber, _errorCorrectionLevel, _dataList);
      }

      mapData(_dataCache, maskPattern);
    };

    var setupPositionProbePattern = function(row, col) {

      for (var r = -1; r <= 7; r += 1) {

        if (row + r <= -1 || _moduleCount <= row + r) continue;

        for (var c = -1; c <= 7; c += 1) {

          if (col + c <= -1 || _moduleCount <= col + c) continue;

          if ( (0 <= r && r <= 6 && (c == 0 || c == 6) )
              || (0 <= c && c <= 6 && (r == 0 || r == 6) )
              || (2 <= r && r <= 4 && 2 <= c && c <= 4) ) {
            _modules[row + r][col + c] = true;
          } else {
            _modules[row + r][col + c] = false;
          }
        }
      }
    };

    var getBestMaskPattern = function() {

      var minLostPoint = 0;
      var pattern = 0;

      for (var i = 0; i < 8; i += 1) {

        makeImpl(true, i);

        var lostPoint = QRUtil.getLostPoint(_this);

        if (i == 0 || minLostPoint > lostPoint) {
          minLostPoint = lostPoint;
          pattern = i;
        }
      }

      return pattern;
    };

    var setupTimingPattern = function() {

      for (var r = 8; r < _moduleCount - 8; r += 1) {
        if (_modules[r][6] != null) {
          continue;
        }
        _modules[r][6] = (r % 2 == 0);
      }

      for (var c = 8; c < _moduleCount - 8; c += 1) {
        if (_modules[6][c] != null) {
          continue;
        }
        _modules[6][c] = (c % 2 == 0);
      }
    };

    var setupPositionAdjustPattern = function() {

      var pos = QRUtil.getPatternPosition(_typeNumber);

      for (var i = 0; i < pos.length; i += 1) {

        for (var j = 0; j < pos.length; j += 1) {

          var row = pos[i];
          var col = pos[j];

          if (_modules[row][col] != null) {
            continue;
          }

          for (var r = -2; r <= 2; r += 1) {

            for (var c = -2; c <= 2; c += 1) {

              if (r == -2 || r == 2 || c == -2 || c == 2
                  || (r == 0 && c == 0) ) {
                _modules[row + r][col + c] = true;
              } else {
                _modules[row + r][col + c] = false;
              }
            }
          }
        }
      }
    };

    var setupTypeNumber = function(test) {

      var bits = QRUtil.getBCHTypeNumber(_typeNumber);

      for (var i = 0; i < 18; i += 1) {
        var mod = (!test && ( (bits >> i) & 1) == 1);
        _modules[Math.floor(i / 3)][i % 3 + _moduleCount - 8 - 3] = mod;
      }

      for (var i = 0; i < 18; i += 1) {
        var mod = (!test && ( (bits >> i) & 1) == 1);
        _modules[i % 3 + _moduleCount - 8 - 3][Math.floor(i / 3)] = mod;
      }
    };

    var setupTypeInfo = function(test, maskPattern) {

      var data = (_errorCorrectionLevel << 3) | maskPattern;
      var bits = QRUtil.getBCHTypeInfo(data);

      // vertical
      for (var i = 0; i < 15; i += 1) {

        var mod = (!test && ( (bits >> i) & 1) == 1);

        if (i < 6) {
          _modules[i][8] = mod;
        } else if (i < 8) {
          _modules[i + 1][8] = mod;
        } else {
          _modules[_moduleCount - 15 + i][8] = mod;
        }
      }

      // horizontal
      for (var i = 0; i < 15; i += 1) {

        var mod = (!test && ( (bits >> i) & 1) == 1);

        if (i < 8) {
          _modules[8][_moduleCount - i - 1] = mod;
        } else if (i < 9) {
          _modules[8][15 - i - 1 + 1] = mod;
        } else {
          _modules[8][15 - i - 1] = mod;
        }
      }

      // fixed module
      _modules[_moduleCount - 8][8] = (!test);
    };

    var mapData = function(data, maskPattern) {

      var inc = -1;
      var row = _moduleCount - 1;
      var bitIndex = 7;
      var byteIndex = 0;
      var maskFunc = QRUtil.getMaskFunction(maskPattern);

      for (var col = _moduleCount - 1; col > 0; col -= 2) {

        if (col == 6) col -= 1;

        while (true) {

          for (var c = 0; c < 2; c += 1) {

            if (_modules[row][col - c] == null) {

              var dark = false;

              if (byteIndex < data.length) {
                dark = ( ( (data[byteIndex] >>> bitIndex) & 1) == 1);
              }

              var mask = maskFunc(row, col - c);

              if (mask) {
                dark = !dark;
              }

              _modules[row][col - c] = dark;
              bitIndex -= 1;

              if (bitIndex == -1) {
                byteIndex += 1;
                bitIndex = 7;
              }
            }
          }

          row += inc;

          if (row < 0 || _moduleCount <= row) {
            row -= inc;
            inc = -inc;
            break;
          }
        }
      }
    };

    var createBytes = function(buffer, rsBlocks) {

      var offset = 0;

      var maxDcCount = 0;
      var maxEcCount = 0;

      var dcdata = new Array(rsBlocks.length);
      var ecdata = new Array(rsBlocks.length);

      for (var r = 0; r < rsBlocks.length; r += 1) {

        var dcCount = rsBlocks[r].dataCount;
        var ecCount = rsBlocks[r].totalCount - dcCount;

        maxDcCount = Math.max(maxDcCount, dcCount);
        maxEcCount = Math.max(maxEcCount, ecCount);

        dcdata[r] = new Array(dcCount);

        for (var i = 0; i < dcdata[r].length; i += 1) {
          dcdata[r][i] = 0xff & buffer.getBuffer()[i + offset];
        }
        offset += dcCount;

        var rsPoly = QRUtil.getErrorCorrectPolynomial(ecCount);
        var rawPoly = qrPolynomial(dcdata[r], rsPoly.getLength() - 1);

        var modPoly = rawPoly.mod(rsPoly);
        ecdata[r] = new Array(rsPoly.getLength() - 1);
        for (var i = 0; i < ecdata[r].length; i += 1) {
          var modIndex = i + modPoly.getLength() - ecdata[r].length;
          ecdata[r][i] = (modIndex >= 0)? modPoly.getAt(modIndex) : 0;
        }
      }

      var totalCodeCount = 0;
      for (var i = 0; i < rsBlocks.length; i += 1) {
        totalCodeCount += rsBlocks[i].totalCount;
      }

      var data = new Array(totalCodeCount);
      var index = 0;

      for (var i = 0; i < maxDcCount; i += 1) {
        for (var r = 0; r < rsBlocks.length; r += 1) {
          if (i < dcdata[r].length) {
            data[index] = dcdata[r][i];
            index += 1;
          }
        }
      }

      for (var i = 0; i < maxEcCount; i += 1) {
        for (var r = 0; r < rsBlocks.length; r += 1) {
          if (i < ecdata[r].length) {
            data[index] = ecdata[r][i];
            index += 1;
          }
        }
      }

      return data;
    };

    var createData = function(typeNumber, errorCorrectionLevel, dataList) {

      var rsBlocks = QRRSBlock.getRSBlocks(typeNumber, errorCorrectionLevel);

      var buffer = qrBitBuffer();

      for (var i = 0; i < dataList.length; i += 1) {
        var data = dataList[i];
        buffer.put(data.getMode(), 4);
        buffer.put(data.getLength(), QRUtil.getLengthInBits(data.getMode(), typeNumber) );
        data.write(buffer);
      }

      // calc num max data.
      var totalDataCount = 0;
      for (var i = 0; i < rsBlocks.length; i += 1) {
        totalDataCount += rsBlocks[i].dataCount;
      }

      if (buffer.getLengthInBits() > totalDataCount * 8) {
        throw 'code length overflow. ('
          + buffer.getLengthInBits()
          + '>'
          + totalDataCount * 8
          + ')';
      }

      // end code
      if (buffer.getLengthInBits() + 4 <= totalDataCount * 8) {
        buffer.put(0, 4);
      }

      // padding
      while (buffer.getLengthInBits() % 8 != 0) {
        buffer.putBit(false);
      }

      // padding
      while (true) {

        if (buffer.getLengthInBits() >= totalDataCount * 8) {
          break;
        }
        buffer.put(PAD0, 8);

        if (buffer.getLengthInBits() >= totalDataCount * 8) {
          break;
        }
        buffer.put(PAD1, 8);
      }

      return createBytes(buffer, rsBlocks);
    };

    _this.addData = function(data, mode) {

      mode = mode || 'Byte';

      var newData = null;

      switch(mode) {
      case 'Numeric' :
        newData = qrNumber(data);
        break;
      case 'Alphanumeric' :
        newData = qrAlphaNum(data);
        break;
      case 'Byte' :
        newData = qr8BitByte(data);
        break;
      case 'Kanji' :
        newData = qrKanji(data);
        break;
      default :
        throw 'mode:' + mode;
      }

      _dataList.push(newData);
      _dataCache = null;
    };

    _this.isDark = function(row, col) {
      if (row < 0 || _moduleCount <= row || col < 0 || _moduleCount <= col) {
        throw row + ',' + col;
      }
      return _modules[row][col];
    };

    _this.getModuleCount = function() {
      return _moduleCount;
    };

    _this.make = function() {
      if (_typeNumber < 1) {
        var typeNumber = 1;

        for (; typeNumber < 40; typeNumber++) {
          var rsBlocks = QRRSBlock.getRSBlocks(typeNumber, _errorCorrectionLevel);
          var buffer = qrBitBuffer();

          for (var i = 0; i < _dataList.length; i++) {
            var data = _dataList[i];
            buffer.put(data.getMode(), 4);
            buffer.put(data.getLength(), QRUtil.getLengthInBits(data.getMode(), typeNumber) );
            data.write(buffer);
          }

          var totalDataCount = 0;
          for (var i = 0; i < rsBlocks.length; i++) {
            totalDataCount += rsBlocks[i].dataCount;
          }

          if (buffer.getLengthInBits() <= totalDataCount * 8) {
            break;
          }
        }

        _typeNumber = typeNumber;
      }

      makeImpl(false, getBestMaskPattern() );
    };

    _this.createTableTag = function(cellSize, margin) {

      cellSize = cellSize || 2;
      margin = (typeof margin == 'undefined')? cellSize * 4 : margin;

      var qrHtml = '';

      qrHtml += '<table style="';
      qrHtml += ' border-width: 0px; border-style: none;';
      qrHtml += ' border-collapse: collapse;';
      qrHtml += ' padding: 0px; margin: ' + margin + 'px;';
      qrHtml += '">';
      qrHtml += '<tbody>';

      for (var r = 0; r < _this.getModuleCount(); r += 1) {

        qrHtml += '<tr>';

        for (var c = 0; c < _this.getModuleCount(); c += 1) {
          qrHtml += '<td style="';
          qrHtml += ' border-width: 0px; border-style: none;';
          qrHtml += ' border-collapse: collapse;';
          qrHtml += ' padding: 0px; margin: 0px;';
          qrHtml += ' width: ' + cellSize + 'px;';
          qrHtml += ' height: ' + cellSize + 'px;';
          qrHtml += ' background-color: ';
          qrHtml += _this.isDark(r, c)? '#000000' : '#ffffff';
          qrHtml += ';';
          qrHtml += '"/>';
        }

        qrHtml += '</tr>';
      }

      qrHtml += '</tbody>';
      qrHtml += '</table>';

      return qrHtml;
    };

    _this.createSvgTag = function(cellSize, margin, alt, title) {

      var opts = {};
      if (typeof arguments[0] == 'object') {
        // Called by options.
        opts = arguments[0];
        // overwrite cellSize and margin.
        cellSize = opts.cellSize;
        margin = opts.margin;
        alt = opts.alt;
        title = opts.title;
      }

      cellSize = cellSize || 2;
      margin = (typeof margin == 'undefined')? cellSize * 4 : margin;

      // Compose alt property surrogate
      alt = (typeof alt === 'string') ? {text: alt} : alt || {};
      alt.text = alt.text || null;
      alt.id = (alt.text) ? alt.id || 'qrcode-description' : null;

      // Compose title property surrogate
      title = (typeof title === 'string') ? {text: title} : title || {};
      title.text = title.text || null;
      title.id = (title.text) ? title.id || 'qrcode-title' : null;

      var size = _this.getModuleCount() * cellSize + margin * 2;
      var c, mc, r, mr, qrSvg='', rect;

      rect = 'l' + cellSize + ',0 0,' + cellSize +
        ' -' + cellSize + ',0 0,-' + cellSize + 'z ';

      qrSvg += '<svg version="1.1" xmlns="http://www.w3.org/2000/svg"';
      qrSvg += !opts.scalable ? ' width="' + size + 'px" height="' + size + 'px"' : '';
      qrSvg += ' viewBox="0 0 ' + size + ' ' + size + '" ';
      qrSvg += ' preserveAspectRatio="xMinYMin meet"';
      qrSvg += (title.text || alt.text) ? ' role="img" aria-labelledby="' +
          escapeXml([title.id, alt.id].join(' ').trim() ) + '"' : '';
      qrSvg += '>';
      qrSvg += (title.text) ? '<title id="' + escapeXml(title.id) + '">' +
          escapeXml(title.text) + '</title>' : '';
      qrSvg += (alt.text) ? '<description id="' + escapeXml(alt.id) + '">' +
          escapeXml(alt.text) + '</description>' : '';
      qrSvg += '<rect width="100%" height="100%" fill="white" cx="0" cy="0"/>';
      qrSvg += '<path d="';

      for (r = 0; r < _this.getModuleCount(); r += 1) {
        mr = r * cellSize + margin;
        for (c = 0; c < _this.getModuleCount(); c += 1) {
          if (_this.isDark(r, c) ) {
            mc = c*cellSize+margin;
            qrSvg += 'M' + mc + ',' + mr + rect;
          }
        }
      }

      qrSvg += '" stroke="transparent" fill="black"/>';
      qrSvg += '</svg>';

      return qrSvg;
    };

    _this.createDataURL = function(cellSize, margin) {

      cellSize = cellSize || 2;
      margin = (typeof margin == 'undefined')? cellSize * 4 : margin;

      var size = _this.getModuleCount() * cellSize + margin * 2;
      var min = margin;
      var max = size - margin;

      return createDataURL(size, size, function(x, y) {
        if (min <= x && x < max && min <= y && y < max) {
          var c = Math.floor( (x - min) / cellSize);
          var r = Math.floor( (y - min) / cellSize);
          return _this.isDark(r, c)? 0 : 1;
        } else {
          return 1;
        }
      } );
    };

    _this.createImgTag = function(cellSize, margin, alt) {

      cellSize = cellSize || 2;
      margin = (typeof margin == 'undefined')? cellSize * 4 : margin;

      var size = _this.getModuleCount() * cellSize + margin * 2;

      var img = '';
      img += '<img';
      img += '\u0020src="';
      img += _this.createDataURL(cellSize, margin);
      img += '"';
      img += '\u0020width="';
      img += size;
      img += '"';
      img += '\u0020height="';
      img += size;
      img += '"';
      if (alt) {
        img += '\u0020alt="';
        img += escapeXml(alt);
        img += '"';
      }
      img += '/>';

      return img;
    };

    var escapeXml = function(s) {
      var escaped = '';
      for (var i = 0; i < s.length; i += 1) {
        var c = s.charAt(i);
        switch(c) {
        case '<': escaped += '&lt;'; break;
        case '>': escaped += '&gt;'; break;
        case '&': escaped += '&amp;'; break;
        case '"': escaped += '&quot;'; break;
        default : escaped += c; break;
        }
      }
      return escaped;
    };

    var _createHalfASCII = function(margin) {
      var cellSize = 1;
      margin = (typeof margin == 'undefined')? cellSize * 2 : margin;

      var size = _this.getModuleCount() * cellSize + margin * 2;
      var min = margin;
      var max = size - margin;

      var y, x, r1, r2, p;

      var blocks = {
        '██': '█',
        '█ ': '▀',
        ' █': '▄',
        '  ': ' '
      };

      var blocksLastLineNoMargin = {
        '██': '▀',
        '█ ': '▀',
        ' █': ' ',
        '  ': ' '
      };

      var ascii = '';
      for (y = 0; y < size; y += 2) {
        r1 = Math.floor((y - min) / cellSize);
        r2 = Math.floor((y + 1 - min) / cellSize);
        for (x = 0; x < size; x += 1) {
          p = '█';

          if (min <= x && x < max && min <= y && y < max && _this.isDark(r1, Math.floor((x - min) / cellSize))) {
            p = ' ';
          }

          if (min <= x && x < max && min <= y+1 && y+1 < max && _this.isDark(r2, Math.floor((x - min) / cellSize))) {
            p += ' ';
          }
          else {
            p += '█';
          }

          // Output 2 characters per pixel, to create full square. 1 character per pixels gives only half width of square.
          ascii += (margin < 1 && y+1 >= max) ? blocksLastLineNoMargin[p] : blocks[p];
        }

        ascii += '\n';
      }

      if (size % 2 && margin > 0) {
        return ascii.substring(0, ascii.length - size - 1) + Array(size+1).join('▀');
      }

      return ascii.substring(0, ascii.length-1);
    };

    _this.createASCII = function(cellSize, margin) {
      cellSize = cellSize || 1;

      if (cellSize < 2) {
        return _createHalfASCII(margin);
      }

      cellSize -= 1;
      margin = (typeof margin == 'undefined')? cellSize * 2 : margin;

      var size = _this.getModuleCount() * cellSize + margin * 2;
      var min = margin;
      var max = size - margin;

      var y, x, r, p;

      var white = Array(cellSize+1).join('██');
      var black = Array(cellSize+1).join('  ');

      var ascii = '';
      var line = '';
      for (y = 0; y < size; y += 1) {
        r = Math.floor( (y - min) / cellSize);
        line = '';
        for (x = 0; x < size; x += 1) {
          p = 1;

          if (min <= x && x < max && min <= y && y < max && _this.isDark(r, Math.floor((x - min) / cellSize))) {
            p = 0;
          }

          // Output 2 characters per pixel, to create full square. 1 character per pixels gives only half width of square.
          line += p ? white : black;
        }

        for (r = 0; r < cellSize; r += 1) {
          ascii += line + '\n';
        }
      }

      return ascii.substring(0, ascii.length-1);
    };

    _this.renderTo2dContext = function(context, cellSize) {
      cellSize = cellSize || 2;
      var length = _this.getModuleCount();
      for (var row = 0; row < length; row++) {
        for (var col = 0; col < length; col++) {
          context.fillStyle = _this.isDark(row, col) ? 'black' : 'white';
          context.fillRect(row * cellSize, col * cellSize, cellSize, cellSize);
        }
      }
    }

    return _this;
  };

  //---------------------------------------------------------------------
  // qrcode.stringToBytes
  //---------------------------------------------------------------------

  qrcode.stringToBytesFuncs = {
    'default' : function(s) {
      var bytes = [];
      for (var i = 0; i < s.length; i += 1) {
        var c = s.charCodeAt(i);
        bytes.push(c & 0xff);
      }
      return bytes;
    }
  };

  qrcode.stringToBytes = qrcode.stringToBytesFuncs['default'];

  //---------------------------------------------------------------------
  // qrcode.createStringToBytes
  //---------------------------------------------------------------------

  /**
   * @param unicodeData base64 string of byte array.
   * [16bit Unicode],[16bit Bytes], ...
   * @param numChars
   */
  qrcode.createStringToBytes = function(unicodeData, numChars) {

    // create conversion map.

    var unicodeMap = function() {

      var bin = base64DecodeInputStream(unicodeData);
      var read = function() {
        var b = bin.read();
        if (b == -1) throw 'eof';
        return b;
      };

      var count = 0;
      var unicodeMap = {};
      while (true) {
        var b0 = bin.read();
        if (b0 == -1) break;
        var b1 = read();
        var b2 = read();
        var b3 = read();
        var k = String.fromCharCode( (b0 << 8) | b1);
        var v = (b2 << 8) | b3;
        unicodeMap[k] = v;
        count += 1;
      }
      if (count != numChars) {
        throw count + ' != ' + numChars;
      }

      return unicodeMap;
    }();

    var unknownChar = '?'.charCodeAt(0);

    return function(s) {
      var bytes = [];
      for (var i = 0; i < s.length; i += 1) {
        var c = s.charCodeAt(i);
        if (c < 128) {
          bytes.push(c);
        } else {
          var b = unicodeMap[s.charAt(i)];
          if (typeof b == 'number') {
            if ( (b & 0xff) == b) {
              // 1byte
              bytes.push(b);
            } else {
              // 2bytes
              bytes.push(b >>> 8);
              bytes.push(b & 0xff);
            }
          } else {
            bytes.push(unknownChar);
          }
        }
      }
      return bytes;
    };
  };

  //---------------------------------------------------------------------
  // QRMode
  //---------------------------------------------------------------------

  var QRMode = {
    MODE_NUMBER :    1 << 0,
    MODE_ALPHA_NUM : 1 << 1,
    MODE_8BIT_BYTE : 1 << 2,
    MODE_KANJI :     1 << 3
  };

  //---------------------------------------------------------------------
  // QRErrorCorrectionLevel
  //---------------------------------------------------------------------

  var QRErrorCorrectionLevel = {
    L : 1,
    M : 0,
    Q : 3,
    H : 2
  };

  //---------------------------------------------------------------------
  // QRMaskPattern
  //---------------------------------------------------------------------

  var QRMaskPattern = {
    PATTERN000 : 0,
    PATTERN001 : 1,
    PATTERN010 : 2,
    PATTERN011 : 3,
    PATTERN100 : 4,
    PATTERN101 : 5,
    PATTERN110 : 6,
    PATTERN111 : 7
  };

  //---------------------------------------------------------------------
  // QRUtil
  //---------------------------------------------------------------------

  var QRUtil = function() {

    var PATTERN_POSITION_TABLE = [
      [],
      [6, 18],
      [6, 22],
      [6, 26],
      [6, 30],
      [6, 34],
      [6, 22, 38],
      [6, 24, 42],
      [6, 26, 46],
      [6, 28, 50],
      [6, 30, 54],
      [6, 32, 58],
      [6, 34, 62],
      [6, 26, 46, 66],
      [6, 26, 48, 70],
      [6, 26, 50, 74],
      [6, 30, 54, 78],
      [6, 30, 56, 82],
      [6, 30, 58, 86],
      [6, 34, 62, 90],
      [6, 28, 50, 72, 94],
      [6, 26, 50, 74, 98],
      [6, 30, 54, 78, 102],
      [6, 28, 54, 80, 106],
      [6, 32, 58, 84, 110],
      [6, 30, 58, 86, 114],
      [6, 34, 62, 90, 118],
      [6, 26, 50, 74, 98, 122],
      [6, 30, 54, 78, 102, 126],
      [6, 26, 52, 78, 104, 130],
      [6, 30, 56, 82, 108, 134],
      [6, 34, 60, 86, 112, 138],
      [6, 30, 58, 86, 114, 142],
      [6, 34, 62, 90, 118, 146],
      [6, 30, 54, 78, 102, 126, 150],
      [6, 24, 50, 76, 102, 128, 154],
      [6, 28, 54, 80, 106, 132, 158],
      [6, 32, 58, 84, 110, 136, 162],
      [6, 26, 54, 82, 110, 138, 166],
      [6, 30, 58, 86, 114, 142, 170]
    ];
    var G15 = (1 << 10) | (1 << 8) | (1 << 5) | (1 << 4) | (1 << 2) | (1 << 1) | (1 << 0);
    var G18 = (1 << 12) | (1 << 11) | (1 << 10) | (1 << 9) | (1 << 8) | (1 << 5) | (1 << 2) | (1 << 0);
    var G15_MASK = (1 << 14) | (1 << 12) | (1 << 10) | (1 << 4) | (1 << 1);

    var _this = {};

    var getBCHDigit = function(data) {
      var digit = 0;
      while (data != 0) {
        digit += 1;
        data >>>= 1;
      }
      return digit;
    };

    _this.getBCHTypeInfo = function(data) {
      var d = data << 10;
      while (getBCHDigit(d) - getBCHDigit(G15) >= 0) {
        d ^= (G15 << (getBCHDigit(d) - getBCHDigit(G15) ) );
      }
      return ( (data << 10) | d) ^ G15_MASK;
    };

    _this.getBCHTypeNumber = function(data) {
      var d = data << 12;
      while (getBCHDigit(d) - getBCHDigit(G18) >= 0) {
        d ^= (G18 << (getBCHDigit(d) - getBCHDigit(G18) ) );
      }
      return (data << 12) | d;
    };

    _this.getPatternPosition = function(typeNumber) {
      return PATTERN_POSITION_TABLE[typeNumber - 1];
    };

    _this.getMaskFunction = function(maskPattern) {

      switch (maskPattern) {

      case QRMaskPattern.PATTERN000 :
        return function(i, j) { return (i + j) % 2 == 0; };
      case QRMaskPattern.PATTERN001 :
        return function(i, j) { return i % 2 == 0; };
      case QRMaskPattern.PATTERN010 :
        return function(i, j) { return j % 3 == 0; };
      case QRMaskPattern.PATTERN011 :
        return function(i, j) { return (i + j) % 3 == 0; };
      case QRMaskPattern.PATTERN100 :
        return function(i, j) { return (Math.floor(i / 2) + Math.floor(j / 3) ) % 2 == 0; };
      case QRMaskPattern.PATTERN101 :
        return function(i, j) { return (i * j) % 2 + (i * j) % 3 == 0; };
      case QRMaskPattern.PATTERN110 :
        return function(i, j) { return ( (i * j) % 2 + (i * j) % 3) % 2 == 0; };
      case QRMaskPattern.PATTERN111 :
        return function(i, j) { return ( (i * j) % 3 + (i + j) % 2) % 2 == 0; };

      default :
        throw 'bad maskPattern:' + maskPattern;
      }
    };

    _this.getErrorCorrectPolynomial = function(errorCorrectLength) {
      var a = qrPolynomial([1], 0);
      for (var i = 0; i < errorCorrectLength; i += 1) {
        a = a.multiply(qrPolynomial([1, QRMath.gexp(i)], 0) );
      }
      return a;
    };

    _this.getLengthInBits = function(mode, type) {

      if (1 <= type && type < 10) {

        // 1 - 9

        switch(mode) {
        case QRMode.MODE_NUMBER    : return 10;
        case QRMode.MODE_ALPHA_NUM : return 9;
        case QRMode.MODE_8BIT_BYTE : return 8;
        case QRMode.MODE_KANJI     : return 8;
        default :
          throw 'mode:' + mode;
        }

      } else if (type < 27) {

        // 10 - 26

        switch(mode) {
        case QRMode.MODE_NUMBER    : return 12;
        case QRMode.MODE_ALPHA_NUM : return 11;
        case QRMode.MODE_8BIT_BYTE : return 16;
        case QRMode.MODE_KANJI     : return 10;
        default :
          throw 'mode:' + mode;
        }

      } else if (type < 41) {

        // 27 - 40

        switch(mode) {
        case QRMode.MODE_NUMBER    : return 14;
        case QRMode.MODE_ALPHA_NUM : return 13;
        case QRMode.MODE_8BIT_BYTE : return 16;
        case QRMode.MODE_KANJI     : return 12;
        default :
          throw 'mode:' + mode;
        }

      } else {
        throw 'type:' + type;
      }
    };

    _this.getLostPoint = function(qrcode) {

      var moduleCount = qrcode.getModuleCount();

      var lostPoint = 0;

      // LEVEL1

      for (var row = 0; row < moduleCount; row += 1) {
        for (var col = 0; col < moduleCount; col += 1) {

          var sameCount = 0;
          var dark = qrcode.isDark(row, col);

          for (var r = -1; r <= 1; r += 1) {

            if (row + r < 0 || moduleCount <= row + r) {
              continue;
            }

            for (var c = -1; c <= 1; c += 1) {

              if (col + c < 0 || moduleCount <= col + c) {
                continue;
              }

              if (r == 0 && c == 0) {
                continue;
              }

              if (dark == qrcode.isDark(row + r, col + c) ) {
                sameCount += 1;
              }
            }
          }

          if (sameCount > 5) {
            lostPoint += (3 + sameCount - 5);
          }
        }
      };

      // LEVEL2

      for (var row = 0; row < moduleCount - 1; row += 1) {
        for (var col = 0; col < moduleCount - 1; col += 1) {
          var count = 0;
          if (qrcode.isDark(row, col) ) count += 1;
          if (qrcode.isDark(row + 1, col) ) count += 1;
          if (qrcode.isDark(row, col + 1) ) count += 1;
          if (qrcode.isDark(row + 1, col + 1) ) count += 1;
          if (count == 0 || count == 4) {
            lostPoint += 3;
          }
        }
      }

      // LEVEL3

      for (var row = 0; row < moduleCount; row += 1) {
        for (var col = 0; col < moduleCount - 6; col += 1) {
          if (qrcode.isDark(row, col)
              && !qrcode.isDark(row, col + 1)
              &&  qrcode.isDark(row, col + 2)
              &&  qrcode.isDark(row, col + 3)
              &&  qrcode.isDark(row, col + 4)
              && !qrcode.isDark(row, col + 5)
              &&  qrcode.isDark(row, col + 6) ) {
            lostPoint += 40;
          }
        }
      }

      for (var col = 0; col < moduleCount; col += 1) {
        for (var row = 0; row < moduleCount - 6; row += 1) {
          if (qrcode.isDark(row, col)
              && !qrcode.isDark(row + 1, col)
              &&  qrcode.isDark(row + 2, col)
              &&  qrcode.isDark(row + 3, col)
              &&  qrcode.isDark(row + 4, col)
              && !qrcode.isDark(row + 5, col)
              &&  qrcode.isDark(row + 6, col) ) {
            lostPoint += 40;
          }
        }
      }

      // LEVEL4

      var darkCount = 0;

      for (var col = 0; col < moduleCount; col += 1) {
        for (var row = 0; row < moduleCount; row += 1) {
          if (qrcode.isDark(row, col) ) {
            darkCount += 1;
          }
        }
      }

      var ratio = Math.abs(100 * darkCount / moduleCount / moduleCount - 50) / 5;
      lostPoint += ratio * 10;

      return lostPoint;
    };

    return _this;
  }();

  //---------------------------------------------------------------------
  // QRMath
  //---------------------------------------------------------------------

  var QRMath = function() {

    var EXP_TABLE = new Array(256);
    var LOG_TABLE = new Array(256);

    // initialize tables
    for (var i = 0; i < 8; i += 1) {
      EXP_TABLE[i] = 1 << i;
    }
    for (var i = 8; i < 256; i += 1) {
      EXP_TABLE[i] = EXP_TABLE[i - 4]
        ^ EXP_TABLE[i - 5]
        ^ EXP_TABLE[i - 6]
        ^ EXP_TABLE[i - 8];
    }
    for (var i = 0; i < 255; i += 1) {
      LOG_TABLE[EXP_TABLE[i] ] = i;
    }

    var _this = {};

    _this.glog = function(n) {

      if (n < 1) {
        throw 'glog(' + n + ')';
      }

      return LOG_TABLE[n];
    };

    _this.gexp = function(n) {

      while (n < 0) {
        n += 255;
      }

      while (n >= 256) {
        n -= 255;
      }

      return EXP_TABLE[n];
    };

    return _this;
  }();

  //---------------------------------------------------------------------
  // qrPolynomial
  //---------------------------------------------------------------------

  function qrPolynomial(num, shift) {

    if (typeof num.length == 'undefined') {
      throw num.length + '/' + shift;
    }

    var _num = function() {
      var offset = 0;
      while (offset < num.length && num[offset] == 0) {
        offset += 1;
      }
      var _num = new Array(num.length - offset + shift);
      for (var i = 0; i < num.length - offset; i += 1) {
        _num[i] = num[i + offset];
      }
      return _num;
    }();

    var _this = {};

    _this.getAt = function(index) {
      return _num[index];
    };

    _this.getLength = function() {
      return _num.length;
    };

    _this.multiply = function(e) {

      var num = new Array(_this.getLength() + e.getLength() - 1);

      for (var i = 0; i < _this.getLength(); i += 1) {
        for (var j = 0; j < e.getLength(); j += 1) {
          num[i + j] ^= QRMath.gexp(QRMath.glog(_this.getAt(i) ) + QRMath.glog(e.getAt(j) ) );
        }
      }

      return qrPolynomial(num, 0);
    };

    _this.mod = function(e) {

      if (_this.getLength() - e.getLength() < 0) {
        return _this;
      }

      var ratio = QRMath.glog(_this.getAt(0) ) - QRMath.glog(e.getAt(0) );

      var num = new Array(_this.getLength() );
      for (var i = 0; i < _this.getLength(); i += 1) {
        num[i] = _this.getAt(i);
      }

      for (var i = 0; i < e.getLength(); i += 1) {
        num[i] ^= QRMath.gexp(QRMath.glog(e.getAt(i) ) + ratio);
      }

      // recursive call
      return qrPolynomial(num, 0).mod(e);
    };

    return _this;
  };

  //---------------------------------------------------------------------
  // QRRSBlock
  //---------------------------------------------------------------------

  var QRRSBlock = function() {

    var RS_BLOCK_TABLE = [

      // L
      // M
      // Q
      // H

      // 1
      [1, 26, 19],
      [1, 26, 16],
      [1, 26, 13],
      [1, 26, 9],

      // 2
      [1, 44, 34],
      [1, 44, 28],
      [1, 44, 22],
      [1, 44, 16],

      // 3
      [1, 70, 55],
      [1, 70, 44],
      [2, 35, 17],
      [2, 35, 13],

      // 4
      [1, 100, 80],
      [2, 50, 32],
      [2, 50, 24],
      [4, 25, 9],

      // 5
      [1, 134, 108],
      [2, 67, 43],
      [2, 33, 15, 2, 34, 16],
      [2, 33, 11, 2, 34, 12],

      // 6
      [2, 86, 68],
      [4, 43, 27],
      [4, 43, 19],
      [4, 43, 15],

      // 7
      [2, 98, 78],
      [4, 49, 31],
      [2, 32, 14, 4, 33, 15],
      [4, 39, 13, 1, 40, 14],

      // 8
      [2, 121, 97],
      [2, 60, 38, 2, 61, 39],
      [4, 40, 18, 2, 41, 19],
      [4, 40, 14, 2, 41, 15],

      // 9
      [2, 146, 116],
      [3, 58, 36, 2, 59, 37],
      [4, 36, 16, 4, 37, 17],
      [4, 36, 12, 4, 37, 13],

      // 10
      [2, 86, 68, 2, 87, 69],
      [4, 69, 43, 1, 70, 44],
      [6, 43, 19, 2, 44, 20],
      [6, 43, 15, 2, 44, 16],

      // 11
      [4, 101, 81],
      [1, 80, 50, 4, 81, 51],
      [4, 50, 22, 4, 51, 23],
      [3, 36, 12, 8, 37, 13],

      // 12
      [2, 116, 92, 2, 117, 93],
      [6, 58, 36, 2, 59, 37],
      [4, 46, 20, 6, 47, 21],
      [7, 42, 14, 4, 43, 15],

      // 13
      [4, 133, 107],
      [8, 59, 37, 1, 60, 38],
      [8, 44, 20, 4, 45, 21],
      [12, 33, 11, 4, 34, 12],

      // 14
      [3, 145, 115, 1, 146, 116],
      [4, 64, 40, 5, 65, 41],
      [11, 36, 16, 5, 37, 17],
      [11, 36, 12, 5, 37, 13],

      // 15
      [5, 109, 87, 1, 110, 88],
      [5, 65, 41, 5, 66, 42],
      [5, 54, 24, 7, 55, 25],
      [11, 36, 12, 7, 37, 13],

      // 16
      [5, 122, 98, 1, 123, 99],
      [7, 73, 45, 3, 74, 46],
      [15, 43, 19, 2, 44, 20],
      [3, 45, 15, 13, 46, 16],

      // 17
      [1, 135, 107, 5, 136, 108],
      [10, 74, 46, 1, 75, 47],
      [1, 50, 22, 15, 51, 23],
      [2, 42, 14, 17, 43, 15],

      // 18
      [5, 150, 120, 1, 151, 121],
      [9, 69, 43, 4, 70, 44],
      [17, 50, 22, 1, 51, 23],
      [2, 42, 14, 19, 43, 15],

      // 19
      [3, 141, 113, 4, 142, 114],
      [3, 70, 44, 11, 71, 45],
      [17, 47, 21, 4, 48, 22],
      [9, 39, 13, 16, 40, 14],

      // 20
      [3, 135, 107, 5, 136, 108],
      [3, 67, 41, 13, 68, 42],
      [15, 54, 24, 5, 55, 25],
      [15, 43, 15, 10, 44, 16],

      // 21
      [4, 144, 116, 4, 145, 117],
      [17, 68, 42],
      [17, 50, 22, 6, 51, 23],
      [19, 46, 16, 6, 47, 17],

      // 22
      [2, 139, 111, 7, 140, 112],
      [17, 74, 46],
      [7, 54, 24, 16, 55, 25],
      [34, 37, 13],

      // 23
      [4, 151, 121, 5, 152, 122],
      [4, 75, 47, 14, 76, 48],
      [11, 54, 24, 14, 55, 25],
      [16, 45, 15, 14, 46, 16],

      // 24
      [6, 147, 117, 4, 148, 118],
      [6, 73, 45, 14, 74, 46],
      [11, 54, 24, 16, 55, 25],
      [30, 46, 16, 2, 47, 17],

      // 25
      [8, 132, 106, 4, 133, 107],
      [8, 75, 47, 13, 76, 48],
      [7, 54, 24, 22, 55, 25],
      [22, 45, 15, 13, 46, 16],

      // 26
      [10, 142, 114, 2, 143, 115],
      [19, 74, 46, 4, 75, 47],
      [28, 50, 22, 6, 51, 23],
      [33, 46, 16, 4, 47, 17],

      // 27
      [8, 152, 122, 4, 153, 123],
      [22, 73, 45, 3, 74, 46],
      [8, 53, 23, 26, 54, 24],
      [12, 45, 15, 28, 46, 16],

      // 28
      [3, 147, 117, 10, 148, 118],
      [3, 73, 45, 23, 74, 46],
      [4, 54, 24, 31, 55, 25],
      [11, 45, 15, 31, 46, 16],

      // 29
      [7, 146, 116, 7, 147, 117],
      [21, 73, 45, 7, 74, 46],
      [1, 53, 23, 37, 54, 24],
      [19, 45, 15, 26, 46, 16],

      // 30
      [5, 145, 115, 10, 146, 116],
      [19, 75, 47, 10, 76, 48],
      [15, 54, 24, 25, 55, 25],
      [23, 45, 15, 25, 46, 16],

      // 31
      [13, 145, 115, 3, 146, 116],
      [2, 74, 46, 29, 75, 47],
      [42, 54, 24, 1, 55, 25],
      [23, 45, 15, 28, 46, 16],

      // 32
      [17, 145, 115],
      [10, 74, 46, 23, 75, 47],
      [10, 54, 24, 35, 55, 25],
      [19, 45, 15, 35, 46, 16],

      // 33
      [17, 145, 115, 1, 146, 116],
      [14, 74, 46, 21, 75, 47],
      [29, 54, 24, 19, 55, 25],
      [11, 45, 15, 46, 46, 16],

      // 34
      [13, 145, 115, 6, 146, 116],
      [14, 74, 46, 23, 75, 47],
      [44, 54, 24, 7, 55, 25],
      [59, 46, 16, 1, 47, 17],

      // 35
      [12, 151, 121, 7, 152, 122],
      [12, 75, 47, 26, 76, 48],
      [39, 54, 24, 14, 55, 25],
      [22, 45, 15, 41, 46, 16],

      // 36
      [6, 151, 121, 14, 152, 122],
      [6, 75, 47, 34, 76, 48],
      [46, 54, 24, 10, 55, 25],
      [2, 45, 15, 64, 46, 16],

      // 37
      [17, 152, 122, 4, 153, 123],
      [29, 74, 46, 14, 75, 47],
      [49, 54, 24, 10, 55, 25],
      [24, 45, 15, 46, 46, 16],

      // 38
      [4, 152, 122, 18, 153, 123],
      [13, 74, 46, 32, 75, 47],
      [48, 54, 24, 14, 55, 25],
      [42, 45, 15, 32, 46, 16],

      // 39
      [20, 147, 117, 4, 148, 118],
      [40, 75, 47, 7, 76, 48],
      [43, 54, 24, 22, 55, 25],
      [10, 45, 15, 67, 46, 16],

      // 40
      [19, 148, 118, 6, 149, 119],
      [18, 75, 47, 31, 76, 48],
      [34, 54, 24, 34, 55, 25],
      [20, 45, 15, 61, 46, 16]
    ];

    var qrRSBlock = function(totalCount, dataCount) {
      var _this = {};
      _this.totalCount = totalCount;
      _this.dataCount = dataCount;
      return _this;
    };

    var _this = {};

    var getRsBlockTable = function(typeNumber, errorCorrectionLevel) {

      switch(errorCorrectionLevel) {
      case QRErrorCorrectionLevel.L :
        return RS_BLOCK_TABLE[(typeNumber - 1) * 4 + 0];
      case QRErrorCorrectionLevel.M :
        return RS_BLOCK_TABLE[(typeNumber - 1) * 4 + 1];
      case QRErrorCorrectionLevel.Q :
        return RS_BLOCK_TABLE[(typeNumber - 1) * 4 + 2];
      case QRErrorCorrectionLevel.H :
        return RS_BLOCK_TABLE[(typeNumber - 1) * 4 + 3];
      default :
        return undefined;
      }
    };

    _this.getRSBlocks = function(typeNumber, errorCorrectionLevel) {

      var rsBlock = getRsBlockTable(typeNumber, errorCorrectionLevel);

      if (typeof rsBlock == 'undefined') {
        throw 'bad rs block @ typeNumber:' + typeNumber +
            '/errorCorrectionLevel:' + errorCorrectionLevel;
      }

      var length = rsBlock.length / 3;

      var list = [];

      for (var i = 0; i < length; i += 1) {

        var count = rsBlock[i * 3 + 0];
        var totalCount = rsBlock[i * 3 + 1];
        var dataCount = rsBlock[i * 3 + 2];

        for (var j = 0; j < count; j += 1) {
          list.push(qrRSBlock(totalCount, dataCount) );
        }
      }

      return list;
    };

    return _this;
  }();

  //---------------------------------------------------------------------
  // qrBitBuffer
  //---------------------------------------------------------------------

  var qrBitBuffer = function() {

    var _buffer = [];
    var _length = 0;

    var _this = {};

    _this.getBuffer = function() {
      return _buffer;
    };

    _this.getAt = function(index) {
      var bufIndex = Math.floor(index / 8);
      return ( (_buffer[bufIndex] >>> (7 - index % 8) ) & 1) == 1;
    };

    _this.put = function(num, length) {
      for (var i = 0; i < length; i += 1) {
        _this.putBit( ( (num >>> (length - i - 1) ) & 1) == 1);
      }
    };

    _this.getLengthInBits = function() {
      return _length;
    };

    _this.putBit = function(bit) {

      var bufIndex = Math.floor(_length / 8);
      if (_buffer.length <= bufIndex) {
        _buffer.push(0);
      }

      if (bit) {
        _buffer[bufIndex] |= (0x80 >>> (_length % 8) );
      }

      _length += 1;
    };

    return _this;
  };

  //---------------------------------------------------------------------
  // qrNumber
  //---------------------------------------------------------------------

  var qrNumber = function(data) {

    var _mode = QRMode.MODE_NUMBER;
    var _data = data;

    var _this = {};

    _this.getMode = function() {
      return _mode;
    };

    _this.getLength = function(buffer) {
      return _data.length;
    };

    _this.write = function(buffer) {

      var data = _data;

      var i = 0;

      while (i + 2 < data.length) {
        buffer.put(strToNum(data.substring(i, i + 3) ), 10);
        i += 3;
      }

      if (i < data.length) {
        if (data.length - i == 1) {
          buffer.put(strToNum(data.substring(i, i + 1) ), 4);
        } else if (data.length - i == 2) {
          buffer.put(strToNum(data.substring(i, i + 2) ), 7);
        }
      }
    };

    var strToNum = function(s) {
      var num = 0;
      for (var i = 0; i < s.length; i += 1) {
        num = num * 10 + chatToNum(s.charAt(i) );
      }
      return num;
    };

    var chatToNum = function(c) {
      if ('0' <= c && c <= '9') {
        return c.charCodeAt(0) - '0'.charCodeAt(0);
      }
      throw 'illegal char :' + c;
    };

    return _this;
  };

  //---------------------------------------------------------------------
  // qrAlphaNum
  //---------------------------------------------------------------------

  var qrAlphaNum = function(data) {

    var _mode = QRMode.MODE_ALPHA_NUM;
    var _data = data;

    var _this = {};

    _this.getMode = function() {
      return _mode;
    };

    _this.getLength = function(buffer) {
      return _data.length;
    };

    _this.write = function(buffer) {

      var s = _data;

      var i = 0;

      while (i + 1 < s.length) {
        buffer.put(
          getCode(s.charAt(i) ) * 45 +
          getCode(s.charAt(i + 1) ), 11);
        i += 2;
      }

      if (i < s.length) {
        buffer.put(getCode(s.charAt(i) ), 6);
      }
    };

    var getCode = function(c) {

      if ('0' <= c && c <= '9') {
        return c.charCodeAt(0) - '0'.charCodeAt(0);
      } else if ('A' <= c && c <= 'Z') {
        return c.charCodeAt(0) - 'A'.charCodeAt(0) + 10;
      } else {
        switch (c) {
        case ' ' : return 36;
        case '$' : return 37;
        case '%' : return 38;
        case '*' : return 39;
        case '+' : return 40;
        case '-' : return 41;
        case '.' : return 42;
        case '/' : return 43;
        case ':' : return 44;
        default :
          throw 'illegal char :' + c;
        }
      }
    };

    return _this;
  };

  //---------------------------------------------------------------------
  // qr8BitByte
  //---------------------------------------------------------------------

  var qr8BitByte = function(data) {

    var _mode = QRMode.MODE_8BIT_BYTE;
    var _data = data;
    var _bytes = qrcode.stringToBytes(data);

    var _this = {};

    _this.getMode = function() {
      return _mode;
    };

    _this.getLength = function(buffer) {
      return _bytes.length;
    };

    _this.write = function(buffer) {
      for (var i = 0; i < _bytes.length; i += 1) {
        buffer.put(_bytes[i], 8);
      }
    };

    return _this;
  };

  //---------------------------------------------------------------------
  // qrKanji
  //---------------------------------------------------------------------

  var qrKanji = function(data) {

    var _mode = QRMode.MODE_KANJI;
    var _data = data;

    var stringToBytes = qrcode.stringToBytesFuncs['SJIS'];
    if (!stringToBytes) {
      throw 'sjis not supported.';
    }
    !function(c, code) {
      // self test for sjis support.
      var test = stringToBytes(c);
      if (test.length != 2 || ( (test[0] << 8) | test[1]) != code) {
        throw 'sjis not supported.';
      }
    }('\u53cb', 0x9746);

    var _bytes = stringToBytes(data);

    var _this = {};

    _this.getMode = function() {
      return _mode;
    };

    _this.getLength = function(buffer) {
      return ~~(_bytes.length / 2);
    };

    _this.write = function(buffer) {

      var data = _bytes;

      var i = 0;

      while (i + 1 < data.length) {

        var c = ( (0xff & data[i]) << 8) | (0xff & data[i + 1]);

        if (0x8140 <= c && c <= 0x9FFC) {
          c -= 0x8140;
        } else if (0xE040 <= c && c <= 0xEBBF) {
          c -= 0xC140;
        } else {
          throw 'illegal char at ' + (i + 1) + '/' + c;
        }

        c = ( (c >>> 8) & 0xff) * 0xC0 + (c & 0xff);

        buffer.put(c, 13);

        i += 2;
      }

      if (i < data.length) {
        throw 'illegal char at ' + (i + 1);
      }
    };

    return _this;
  };

  //=====================================================================
  // GIF Support etc.
  //

  //---------------------------------------------------------------------
  // byteArrayOutputStream
  //---------------------------------------------------------------------

  var byteArrayOutputStream = function() {

    var _bytes = [];

    var _this = {};

    _this.writeByte = function(b) {
      _bytes.push(b & 0xff);
    };

    _this.writeShort = function(i) {
      _this.writeByte(i);
      _this.writeByte(i >>> 8);
    };

    _this.writeBytes = function(b, off, len) {
      off = off || 0;
      len = len || b.length;
      for (var i = 0; i < len; i += 1) {
        _this.writeByte(b[i + off]);
      }
    };

    _this.writeString = function(s) {
      for (var i = 0; i < s.length; i += 1) {
        _this.writeByte(s.charCodeAt(i) );
      }
    };

    _this.toByteArray = function() {
      return _bytes;
    };

    _this.toString = function() {
      var s = '';
      s += '[';
      for (var i = 0; i < _bytes.length; i += 1) {
        if (i > 0) {
          s += ',';
        }
        s += _bytes[i];
      }
      s += ']';
      return s;
    };

    return _this;
  };

  //---------------------------------------------------------------------
  // base64EncodeOutputStream
  //---------------------------------------------------------------------

  var base64EncodeOutputStream = function() {

    var _buffer = 0;
    var _buflen = 0;
    var _length = 0;
    var _base64 = '';

    var _this = {};

    var writeEncoded = function(b) {
      _base64 += String.fromCharCode(encode(b & 0x3f) );
    };

    var encode = function(n) {
      if (n < 0) {
        // error.
      } else if (n < 26) {
        return 0x41 + n;
      } else if (n < 52) {
        return 0x61 + (n - 26);
      } else if (n < 62) {
        return 0x30 + (n - 52);
      } else if (n == 62) {
        return 0x2b;
      } else if (n == 63) {
        return 0x2f;
      }
      throw 'n:' + n;
    };

    _this.writeByte = function(n) {

      _buffer = (_buffer << 8) | (n & 0xff);
      _buflen += 8;
      _length += 1;

      while (_buflen >= 6) {
        writeEncoded(_buffer >>> (_buflen - 6) );
        _buflen -= 6;
      }
    };

    _this.flush = function() {

      if (_buflen > 0) {
        writeEncoded(_buffer << (6 - _buflen) );
        _buffer = 0;
        _buflen = 0;
      }

      if (_length % 3 != 0) {
        // padding
        var padlen = 3 - _length % 3;
        for (var i = 0; i < padlen; i += 1) {
          _base64 += '=';
        }
      }
    };

    _this.toString = function() {
      return _base64;
    };

    return _this;
  };

  //---------------------------------------------------------------------
  // base64DecodeInputStream
  //---------------------------------------------------------------------

  var base64DecodeInputStream = function(str) {

    var _str = str;
    var _pos = 0;
    var _buffer = 0;
    var _buflen = 0;

    var _this = {};

    _this.read = function() {

      while (_buflen < 8) {

        if (_pos >= _str.length) {
          if (_buflen == 0) {
            return -1;
          }
          throw 'unexpected end of file./' + _buflen;
        }

        var c = _str.charAt(_pos);
        _pos += 1;

        if (c == '=') {
          _buflen = 0;
          return -1;
        } else if (c.match(/^\s$/) ) {
          // ignore if whitespace.
          continue;
        }

        _buffer = (_buffer << 6) | decode(c.charCodeAt(0) );
        _buflen += 6;
      }

      var n = (_buffer >>> (_buflen - 8) ) & 0xff;
      _buflen -= 8;
      return n;
    };

    var decode = function(c) {
      if (0x41 <= c && c <= 0x5a) {
        return c - 0x41;
      } else if (0x61 <= c && c <= 0x7a) {
        return c - 0x61 + 26;
      } else if (0x30 <= c && c <= 0x39) {
        return c - 0x30 + 52;
      } else if (c == 0x2b) {
        return 62;
      } else if (c == 0x2f) {
        return 63;
      } else {
        throw 'c:' + c;
      }
    };

    return _this;
  };

  //---------------------------------------------------------------------
  // gifImage (B/W)
  //---------------------------------------------------------------------

  var gifImage = function(width, height) {

    var _width = width;
    var _height = height;
    var _data = new Array(width * height);

    var _this = {};

    _this.setPixel = function(x, y, pixel) {
      _data[y * _width + x] = pixel;
    };

    _this.write = function(out) {

      //---------------------------------
      // GIF Signature

      out.writeString('GIF87a');

      //---------------------------------
      // Screen Descriptor

      out.writeShort(_width);
      out.writeShort(_height);

      out.writeByte(0x80); // 2bit
      out.writeByte(0);
      out.writeByte(0);

      //---------------------------------
      // Global Color Map

      // black
      out.writeByte(0x00);
      out.writeByte(0x00);
      out.writeByte(0x00);

      // white
      out.writeByte(0xff);
      out.writeByte(0xff);
      out.writeByte(0xff);

      //---------------------------------
      // Image Descriptor

      out.writeString(',');
      out.writeShort(0);
      out.writeShort(0);
      out.writeShort(_width);
      out.writeShort(_height);
      out.writeByte(0);

      //---------------------------------
      // Local Color Map

      //---------------------------------
      // Raster Data

      var lzwMinCodeSize = 2;
      var raster = getLZWRaster(lzwMinCodeSize);

      out.writeByte(lzwMinCodeSize);

      var offset = 0;

      while (raster.length - offset > 255) {
        out.writeByte(255);
        out.writeBytes(raster, offset, 255);
        offset += 255;
      }

      out.writeByte(raster.length - offset);
      out.writeBytes(raster, offset, raster.length - offset);
      out.writeByte(0x00);

      //---------------------------------
      // GIF Terminator
      out.writeString(';');
    };

    var bitOutputStream = function(out) {

      var _out = out;
      var _bitLength = 0;
      var _bitBuffer = 0;

      var _this = {};

      _this.write = function(data, length) {

        if ( (data >>> length) != 0) {
          throw 'length over';
        }

        while (_bitLength + length >= 8) {
          _out.writeByte(0xff & ( (data << _bitLength) | _bitBuffer) );
          length -= (8 - _bitLength);
          data >>>= (8 - _bitLength);
          _bitBuffer = 0;
          _bitLength = 0;
        }

        _bitBuffer = (data << _bitLength) | _bitBuffer;
        _bitLength = _bitLength + length;
      };

      _this.flush = function() {
        if (_bitLength > 0) {
          _out.writeByte(_bitBuffer);
        }
      };

      return _this;
    };

    var getLZWRaster = function(lzwMinCodeSize) {

      var clearCode = 1 << lzwMinCodeSize;
      var endCode = (1 << lzwMinCodeSize) + 1;
      var bitLength = lzwMinCodeSize + 1;

      // Setup LZWTable
      var table = lzwTable();

      for (var i = 0; i < clearCode; i += 1) {
        table.add(String.fromCharCode(i) );
      }
      table.add(String.fromCharCode(clearCode) );
      table.add(String.fromCharCode(endCode) );

      var byteOut = byteArrayOutputStream();
      var bitOut = bitOutputStream(byteOut);

      // clear code
      bitOut.write(clearCode, bitLength);

      var dataIndex = 0;

      var s = String.fromCharCode(_data[dataIndex]);
      dataIndex += 1;

      while (dataIndex < _data.length) {

        var c = String.fromCharCode(_data[dataIndex]);
        dataIndex += 1;

        if (table.contains(s + c) ) {

          s = s + c;

        } else {

          bitOut.write(table.indexOf(s), bitLength);

          if (table.size() < 0xfff) {

            if (table.size() == (1 << bitLength) ) {
              bitLength += 1;
            }

            table.add(s + c);
          }

          s = c;
        }
      }

      bitOut.write(table.indexOf(s), bitLength);

      // end code
      bitOut.write(endCode, bitLength);

      bitOut.flush();

      return byteOut.toByteArray();
    };

    var lzwTable = function() {

      var _map = {};
      var _size = 0;

      var _this = {};

      _this.add = function(key) {
        if (_this.contains(key) ) {
          throw 'dup key:' + key;
        }
        _map[key] = _size;
        _size += 1;
      };

      _this.size = function() {
        return _size;
      };

      _this.indexOf = function(key) {
        return _map[key];
      };

      _this.contains = function(key) {
        return typeof _map[key] != 'undefined';
      };

      return _this;
    };

    return _this;
  };

  var createDataURL = function(width, height, getPixel) {
    var gif = gifImage(width, height);
    for (var y = 0; y < height; y += 1) {
      for (var x = 0; x < width; x += 1) {
        gif.setPixel(x, y, getPixel(x, y) );
      }
    }

    var b = byteArrayOutputStream();
    gif.write(b);

    var base64 = base64EncodeOutputStream();
    var bytes = b.toByteArray();
    for (var i = 0; i < bytes.length; i += 1) {
      base64.writeByte(bytes[i]);
    }
    base64.flush();

    return 'data:image/gif;base64,' + base64;
  };

  //---------------------------------------------------------------------
  // returns qrcode function.

  return qrcode;
}();

// multibyte support
!function() {

  qrcode.stringToBytesFuncs['UTF-8'] = function(s) {
    // http://stackoverflow.com/questions/18729405/how-to-convert-utf8-string-to-byte-array
    function toUTF8Array(str) {
      var utf8 = [];
      for (var i=0; i < str.length; i++) {
        var charcode = str.charCodeAt(i);
        if (charcode < 0x80) utf8.push(charcode);
        else if (charcode < 0x800) {
          utf8.push(0xc0 | (charcode >> 6),
              0x80 | (charcode & 0x3f));
        }
        else if (charcode < 0xd800 || charcode >= 0xe000) {
          utf8.push(0xe0 | (charcode >> 12),
              0x80 | ((charcode>>6) & 0x3f),
              0x80 | (charcode & 0x3f));
        }
        // surrogate pair
        else {
          i++;
          // UTF-16 encodes 0x10000-0x10FFFF by
          // subtracting 0x10000 and splitting the
          // 20 bits of 0x0-0xFFFFF into two halves
          charcode = 0x10000 + (((charcode & 0x3ff)<<10)
            | (str.charCodeAt(i) & 0x3ff));
          utf8.push(0xf0 | (charcode >>18),
              0x80 | ((charcode>>12) & 0x3f),
              0x80 | ((charcode>>6) & 0x3f),
              0x80 | (charcode & 0x3f));
        }
      }
      return utf8;
    }
    return toUTF8Array(s);
  };

}();

(function (factory) {
  if (typeof define === 'function' && define.amd) {
      define([], factory);
  } else if (typeof exports === 'object') {
      module.exports = factory();
  }
}(function () {
    return qrcode;
}));

;
/* Renal Care Academy: certificate of completion (Dr. Rivero, Nov 27 2026).
 *
 * On a track's end-of-course examination page: when the learner passes (80% or the page's own "Passed" verdict),
 * a "Get your certificate" panel appears under the result. The learner types the name to print; the certificate is
 * drawn in the browser (canvas) and can be saved as an image or printed / saved as PDF.
 * No account or login. The certificate is registered at /api/certs (name, track, date, score), so its QR code opens
 * /verify?c=<code>; offline or when registration fails, the learner still gets an unregistered copy without a QR code.
 * It is a self-study certificate of completion, NOT CPD-accredited, and says so on its face.
 *
 * Edit this file; tools/academy/apply_certificate.py bundles it after assets/vendor/qrcode-generator.js (MIT) and
 * fingerprints the bundle (assets/academy-certificate.<hash>.js) and tags
 * the end-of-course examination pages.
 */
(function () {
  "use strict";
  var result = document.getElementById("nc-result");
  var form = document.getElementById("nc-quiz");
  if (!result || !form) return;

  var PASS = 0.8;
  var DISTINCTION = 0.95;   // 38 of 40 or better: "with distinction"
  var MEDAL = '<svg class="rcm-cert-medal" viewBox="0 0 64 64" aria-hidden="true"><path d="M20 4h10l6 18h-10z" fill="#1a6b72"/><path d="M44 4H34l-6 18h10z" fill="#1b2f55"/>' +
    '<circle cx="32" cy="40" r="20" fill="#d2ad52" stroke="#9c7422" stroke-width="2"/><circle cx="32" cy="40" r="14" fill="none" stroke="#fff3c4" stroke-width="1.5"/>' +
    '<path d="M32 30l3 6.2 6.8.9-5 4.7 1.3 6.7L32 45.3l-6.1 3.2 1.3-6.7-5-4.7 6.8-.9z" fill="#fff8e1"/></svg>';
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  // A short burst of confetti over the panel (skipped for reduced motion and E-paper).
  function celebrate(host) {
    if (matchMedia("(prefers-reduced-motion: reduce)").matches || document.documentElement.getAttribute("data-shade") === "epaper") return;
    var cv = document.createElement("canvas"), r = host.getBoundingClientRect();
    cv.className = "rcm-confetti"; cv.setAttribute("aria-hidden", "true");
    var dpr = Math.min(2, window.devicePixelRatio || 1), w = innerWidth, h = innerHeight;
    cv.width = w * dpr; cv.height = h * dpr; document.body.appendChild(cv);
    var ctx = cv.getContext("2d"); ctx.scale(dpr, dpr);
    var cols = ["#d2ad52", "#f3dc94", "#1a6b72", "#1b2f55", "#c55a11", "#4fb3b8"], ps = [];
    var ox = Math.max(40, Math.min(w - 40, r.left + r.width / 2)), oy = Math.max(60, Math.min(h - 60, r.top + 40));
    for (var i = 0; i < 140; i++) {
      var a = -Math.PI / 2 + (Math.random() - 0.5) * 2.2, v = 7 + Math.random() * 9;
      ps.push({ x: ox, y: oy, vx: Math.cos(a) * v, vy: Math.sin(a) * v, s: 5 + Math.random() * 6, r: Math.random() * 6,
                vr: (Math.random() - 0.5) * 0.4, c: cols[i % cols.length] });
    }
    var t0 = performance.now();
    (function tick(t) {
      var el = t - t0; ctx.clearRect(0, 0, w, h);
      ps.forEach(function (p) {
        p.vy += 0.32; p.vx *= 0.99; p.x += p.vx; p.y += p.vy; p.r += p.vr;
        ctx.save(); ctx.globalAlpha = Math.max(0, 1 - el / 2600); ctx.translate(p.x, p.y); ctx.rotate(p.r);
        ctx.fillStyle = p.c; ctx.fillRect(-p.s / 2, -p.s / 4, p.s, p.s / 2); ctx.restore();
      });
      if (el < 2600) requestAnimationFrame(tick); else cv.remove();
    })(t0);
  }
  var API = "/api/certs", VERIFY = "https://renalcarematters.com/verify?c=";
  var me = document.currentScript;
  var STUDY_MIN = me ? +me.getAttribute("data-study-min") || 0 : 0;

  // Time on the examination: from the first answer to "Check answers" (a new set of questions restarts it).
  var started = 0, examMin = 0;
  form.addEventListener("change", function () { if (!started) started = Date.now(); });
  form.addEventListener("submit", function () { if (started) examMin = Math.max(1, Math.round((Date.now() - started) / 60000)); }, true);
  form.addEventListener("click", function (e) { if (e.target.closest("[data-nc-newset]")) { started = 0; examMin = 0; } });
  function hm(min) {
    var h = Math.floor(min / 60), m = min % 60;
    return (h ? h + (h === 1 ? " hour" : " hours") : "") + (h && m ? " " : "") + (m ? m + " minutes" : "");
  }
  var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
    "November", "December"];

  function txt(el) { return el ? (el.textContent || "").replace(/\s+/g, " ").trim() : ""; }

  // Track name: the last link in the breadcrumb (the track hub), e.g. "Dialysis Technician".
  function trackName() {
    var links = document.querySelectorAll(".nc-bar a");
    var a = links[links.length - 1];
    return a && a.getAttribute("href") !== "./" ? txt(a) : txt(document.querySelector("h1"));
  }
  function moduleCount() {
    var given = me ? +me.getAttribute("data-modules") || 0 : 0;   // module pages counted by the patcher
    if (given) return given;
    var n = 0;
    document.querySelectorAll("#about table tbody tr").forEach(function (r) {
      if (/^\s*\d+\s*$/.test(txt(r.cells[0]))) n++;   // numbered module rows only, not the Total row
    });
    return n;
  }

  // Did the learner pass? Use the page's own verdict when it gives one (nursing exams have safety-critical items).
  function passed() {
    var t = txt(result);
    if (/not yet passed/i.test(t)) return null;
    var m = t.match(/(\d+)\s+of\s+(\d+)/);
    if (!m) return null;
    var score = +m[1], total = +m[2];
    if (!total) return null;
    if (/\bpassed\b/i.test(t) || score / total >= PASS) return { score: score, total: total };
    return null;
  }

  function today() {
    var d = new Date();
    return { text: MONTHS[d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear(),
             iso: d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2) };
  }

  // A short certificate code from the name, track, date and score (SHA-256, first 8 hex digits).
  function code(name, track, iso, score, total) {
    var raw = [name.toLowerCase(), track, iso, score + "/" + total].join("|");
    var initials = track.split(/\s+/).map(function (w) { return w.charAt(0); }).join("").toUpperCase().replace(/[^A-Z]/g, "").slice(0, 4) || "X";
    var fallback = function () {
      var h = 5381; for (var i = 0; i < raw.length; i++) h = ((h << 5) + h + raw.charCodeAt(i)) >>> 0;
      return Promise.resolve(("00000000" + h.toString(16)).slice(-8));
    };
    var p = (window.crypto && crypto.subtle && window.TextEncoder)
      ? crypto.subtle.digest("SHA-256", new TextEncoder().encode(raw)).then(function (buf) {
          return Array.prototype.map.call(new Uint8Array(buf).slice(0, 4), function (b) { return ("0" + b.toString(16)).slice(-2); }).join("");
        }, fallback)
      : fallback();
    return p.then(function (hex) { return "RCA-" + initials + "-" + iso.replace(/-/g, "").slice(2) + "-" + hex.toUpperCase(); });
  }

  /* ---------- drawing ---------- */
  var W = 2000, H = 1414;   // A4 landscape proportions
  var NAVY = "#1b2f55", TEAL = "#1a6b72", GOLD = "#b08a2e", GOLD2 = "#d9b862", INK = "#1e2a38", MUTED = "#5a6678";
  var SANS = "Inter, Manrope, 'Helvetica Neue', Arial, sans-serif";
  var SERIF = "Georgia, 'Times New Roman', 'Noto Serif', serif";

  function fit(ctx, text, maxW, size, weight, family) {
    var s = size;
    do { ctx.font = weight + " " + s + "px " + family; if (ctx.measureText(text).width <= maxW) break; s -= 2; } while (s > 18);
    return s;
  }
  function wrap(ctx, text, x, y, maxW, lineH) {
    var words = text.split(" "), line = "", lines = [];
    words.forEach(function (w) {
      var t = line ? line + " " + w : w;
      if (ctx.measureText(t).width > maxW && line) { lines.push(line); line = w; } else line = t;
    });
    if (line) lines.push(line);
    lines.forEach(function (l, i) { ctx.fillText(l, x, y + i * lineH); });
    return lines.length;
  }
  // Letter-spaced text, centered on x.
  function spaced(ctx, text, x, y, gap) {
    var w = 0, i;
    for (i = 0; i < text.length; i++) w += ctx.measureText(text[i]).width + (i ? gap : 0);
    var cx = x - w / 2, al = ctx.textAlign; ctx.textAlign = "left";
    for (i = 0; i < text.length; i++) { ctx.fillText(text[i], cx, y); cx += ctx.measureText(text[i]).width + gap; }
    ctx.textAlign = al;
    return w;
  }
  // Text set around a circle (top arc), centered at angle -90°.
  function arcText(ctx, text, cx, cy, r, gap) {
    var widths = [], total = 0, i;
    for (i = 0; i < text.length; i++) { widths.push(ctx.measureText(text[i]).width); total += widths[i] + gap; }
    var a = -Math.PI / 2 - total / r / 2;
    ctx.save(); ctx.textAlign = "center"; ctx.textBaseline = "middle";
    for (i = 0; i < text.length; i++) {
      var aw = (widths[i] + gap) / r;
      ctx.save(); ctx.translate(cx + r * Math.cos(a + aw / 2), cy + r * Math.sin(a + aw / 2)); ctx.rotate(a + aw / 2 + Math.PI / 2);
      ctx.fillText(text[i], 0, 0); ctx.restore();
      a += aw;
    }
    ctx.restore();
  }
  // Interlaced sine waves along a straight edge (guilloche band).
  function wave(ctx, x1, y1, x2, y2, amp, period) {
    var len = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / len, uy = (y2 - y1) / len, nx = -uy, ny = ux;
    [0, Math.PI].forEach(function (ph) {
      ctx.beginPath();
      for (var t = 0; t <= len; t += 2) {
        var o = amp * Math.sin(2 * Math.PI * t / period + ph);
        var px = x1 + ux * t + nx * o, py = y1 + uy * t + ny * o;
        t ? ctx.lineTo(px, py) : ctx.moveTo(px, py);
      }
      ctx.stroke();
    });
  }
  // Guilloche rosette: elliptical petals that all pass through the center, so it has no hollow disc.
  function rosette(ctx, cx, cy, R, n, alpha) {
    ctx.save(); ctx.translate(cx, cy); ctx.strokeStyle = "rgba(176,138,46," + alpha + ")"; ctx.lineWidth = 1.3;
    for (var i = 0; i < n; i++) {
      ctx.rotate(2 * Math.PI / n);
      ctx.beginPath(); ctx.ellipse(R / 2, 0, R / 2, R * 0.16, 0, 0, 2 * Math.PI); ctx.stroke();
    }
    ctx.restore();
  }
  function diamond(ctx, x, y, r, fill, stroke) {
    ctx.beginPath(); ctx.moveTo(x, y - r); ctx.lineTo(x + r, y); ctx.lineTo(x, y + r); ctx.lineTo(x - r, y); ctx.closePath();
    ctx.fillStyle = fill; ctx.fill(); if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = 2; ctx.stroke(); }
  }
  function goldGrad(ctx, x, y, r) {
    var g = ctx.createRadialGradient(x - r * 0.3, y - r * 0.35, r * 0.1, x, y, r);
    g.addColorStop(0, "#f3dc94"); g.addColorStop(0.55, "#d2ad52"); g.addColorStop(1, "#9c7422");
    return g;
  }

  function seal(ctx, cx, cy, year) {
    var R = 104;
    // ribbon tails
    ctx.fillStyle = NAVY;
    [[-1], [1]].forEach(function (s) {
      var k = s[0];
      ctx.beginPath(); ctx.moveTo(cx + k * 30, cy + 40); ctx.lineTo(cx + k * 78, cy + 168); ctx.lineTo(cx + k * 56, cy + 150);
      ctx.lineTo(cx + k * 40, cy + 176); ctx.lineTo(cx + k * 4, cy + 58); ctx.closePath(); ctx.fill();
    });
    ctx.fillStyle = TEAL;
    [[-1], [1]].forEach(function (s) {
      var k = s[0];
      ctx.beginPath(); ctx.moveTo(cx + k * 22, cy + 52); ctx.lineTo(cx + k * 56, cy + 150); ctx.lineTo(cx + k * 40, cy + 176);
      ctx.lineTo(cx + k * 10, cy + 70); ctx.closePath(); ctx.fill();
    });
    // scalloped gold edge
    ctx.save(); ctx.shadowColor = "rgba(60,40,0,.28)"; ctx.shadowBlur = 14; ctx.shadowOffsetY = 4;
    ctx.beginPath();
    for (var i = 0; i <= 96; i++) {
      var a = i / 96 * 2 * Math.PI, rr = i % 2 ? R - 7 : R;
      i ? ctx.lineTo(cx + rr * Math.cos(a), cy + rr * Math.sin(a)) : ctx.moveTo(cx + rr, cy);
    }
    ctx.closePath(); ctx.fillStyle = goldGrad(ctx, cx, cy, R); ctx.fill(); ctx.restore();
    ctx.strokeStyle = "rgba(255,248,220,.85)"; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.arc(cx, cy, R - 16, 0, 2 * Math.PI); ctx.stroke();
    ctx.strokeStyle = "rgba(110,80,20,.55)"; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.arc(cx, cy, R - 21, 0, 2 * Math.PI); ctx.stroke();
    // navy center
    ctx.fillStyle = NAVY; ctx.beginPath(); ctx.arc(cx, cy, 56, 0, 2 * Math.PI); ctx.fill();
    ctx.strokeStyle = GOLD2; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(cx, cy, 50, 0, 2 * Math.PI); ctx.stroke();
    ctx.fillStyle = "#4a3410"; ctx.font = "700 15px " + SANS;
    arcText(ctx, "RENAL CARE ACADEMY", cx, cy, R - 36, 3.2);
    // lower arc: draw rotated by 180° so it reads left-to-right along the bottom
    ctx.save(); ctx.translate(cx, cy); ctx.rotate(Math.PI);
    ctx.font = "700 13px " + SANS; arcTextInner(ctx, "· SELF-STUDY ·", 0, 0, R - 36, 3); ctx.restore();
    ctx.fillStyle = "#f3dc94"; ctx.textAlign = "center"; ctx.textBaseline = "middle";
    ctx.font = "700 34px " + SERIF; ctx.fillText("RCA", cx, cy - 8);
    ctx.font = "600 15px " + SANS; ctx.fillText(String(year), cx, cy + 24);
    ctx.textBaseline = "alphabetic";
  }
  // Bottom arc text: drawn on the top arc of a canvas rotated 180°, characters flipped so they stand upright.
  function arcTextInner(ctx, text, cx, cy, r, gap) {
    var widths = [], total = 0, i;
    for (i = 0; i < text.length; i++) { widths.push(ctx.measureText(text[i]).width); total += widths[i] + gap; }
    var a = -Math.PI / 2 + total / r / 2;
    ctx.textAlign = "center"; ctx.textBaseline = "middle";
    for (i = 0; i < text.length; i++) {
      var aw = (widths[i] + gap) / r;
      ctx.save(); ctx.translate(cx + r * Math.cos(a - aw / 2), cy + r * Math.sin(a - aw / 2)); ctx.rotate(a - aw / 2 - Math.PI / 2);
      ctx.fillText(text[i], 0, 0); ctx.restore();
      a -= aw;
    }
  }

  function draw(canvas, d) {
    var ctx = canvas.getContext("2d");
    canvas.width = W; canvas.height = H;
    // paper
    var bg = ctx.createRadialGradient(W / 2, H / 2, 200, W / 2, H / 2, 1200);
    bg.addColorStop(0, "#fffdf6"); bg.addColorStop(1, "#f4ecd8");
    ctx.fillStyle = bg; ctx.fillRect(0, 0, W, H);
    rosette(ctx, W / 2, 640, 540, 72, 0.07);

    // frame: navy outer, gold rules, guilloche band, corner diamonds
    ctx.strokeStyle = NAVY; ctx.lineWidth = 20; ctx.strokeRect(30, 30, W - 60, H - 60);
    ctx.strokeStyle = GOLD; ctx.lineWidth = 2.5; ctx.strokeRect(56, 56, W - 112, H - 112);
    ctx.strokeStyle = "rgba(176,138,46,.75)"; ctx.lineWidth = 1.3;
    var b = 74;
    wave(ctx, b, b, W - b, b, 9, 26); wave(ctx, b, H - b, W - b, H - b, 9, 26);
    wave(ctx, b, b, b, H - b, 9, 26); wave(ctx, W - b, b, W - b, H - b, 9, 26);
    ctx.strokeStyle = GOLD; ctx.lineWidth = 2.5; ctx.strokeRect(92, 92, W - 184, H - 184);
    ctx.lineWidth = 1; ctx.strokeRect(100, 100, W - 200, H - 200);
    [[b, b], [W - b, b], [b, H - b], [W - b, H - b]].forEach(function (c) { diamond(ctx, c[0], c[1], 20, NAVY, GOLD2); diamond(ctx, c[0], c[1], 7, GOLD2); });

    ctx.textAlign = "center"; ctx.textBaseline = "alphabetic";
    // academy line with rules
    ctx.fillStyle = NAVY; ctx.font = "700 26px " + SANS;
    var aw = spaced(ctx, "RENAL CARE ACADEMY", W / 2, 196, 7);
    ctx.strokeStyle = GOLD; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(W / 2 - aw / 2 - 150, 187); ctx.lineTo(W / 2 - aw / 2 - 30, 187);
    ctx.moveTo(W / 2 + aw / 2 + 30, 187); ctx.lineTo(W / 2 + aw / 2 + 150, 187); ctx.stroke();
    diamond(ctx, W / 2 - aw / 2 - 158, 187, 5, GOLD); diamond(ctx, W / 2 + aw / 2 + 158, 187, 5, GOLD);
    ctx.fillStyle = MUTED; ctx.font = "500 21px " + SANS;
    spaced(ctx, "RENALCAREMATTERS.COM", W / 2, 232, 4);

    // title
    ctx.fillStyle = NAVY; ctx.font = "400 104px " + SERIF;
    spaced(ctx, "CERTIFICATE", W / 2, 360, 16);
    ctx.fillStyle = GOLD; ctx.font = "italic 400 50px " + SERIF;
    ctx.fillText("of Completion", W / 2, 428);

    ctx.fillStyle = MUTED; ctx.font = "italic 400 34px " + SERIF;
    ctx.fillText("This is to certify that", W / 2, 510);

    // name
    ctx.fillStyle = INK;
    var ns = fit(ctx, d.name, 1360, 96, "italic 700", SERIF);
    ctx.font = "italic 700 " + ns + "px " + SERIF; ctx.fillText(d.name, W / 2, 610);
    var g = ctx.createLinearGradient(W / 2 - 560, 0, W / 2 + 560, 0);
    g.addColorStop(0, "rgba(176,138,46,0)"); g.addColorStop(0.15, GOLD); g.addColorStop(0.85, GOLD); g.addColorStop(1, "rgba(176,138,46,0)");
    ctx.strokeStyle = g; ctx.lineWidth = 2.5;
    ctx.beginPath(); ctx.moveTo(W / 2 - 560, 648); ctx.lineTo(W / 2 + 560, 648); ctx.stroke();
    diamond(ctx, W / 2, 648, 8, GOLD);

    ctx.fillStyle = INK; ctx.font = "400 32px " + SANS;
    var course = "has completed the " + (d.modules ? d.modules + "-module " : "") + "self-study course" +
      (d.studyMin ? " (an estimated " + d.studyMin + " minutes of study)" : "");
    fit(ctx, course, 1500, 32, "400", SANS); ctx.fillText(course, W / 2, 718);
    ctx.fillStyle = NAVY;
    var ts = fit(ctx, d.track, 1500, 60, "800", SANS);
    ctx.font = "800 " + ts + "px " + SANS; ctx.fillText(d.track, W / 2, 796);
    ctx.fillStyle = INK; ctx.font = "400 30px " + SANS;
    var what = "and passed its end-of-course examination with " + d.score + " of " + d.total + " best answers (" +
      Math.round(100 * d.score / d.total) + "%)" + (d.examMin ? " in " + d.examMin + (d.examMin === 1 ? " minute." : " minutes.") : ".");
    wrap(ctx, what, W / 2, 856, 1420, 42);
    if (d.score / d.total >= DISTINCTION) {
      ctx.fillStyle = GOLD; ctx.font = "italic 700 34px " + SERIF; ctx.fillText("— with Distinction —", W / 2, 904);
    }

    // bottom left: date and study time
    function field(x, y, value, label) {
      ctx.fillStyle = INK; fit(ctx, value, 440, 32, "600", SANS); ctx.fillText(value, x, y);
      ctx.strokeStyle = "rgba(27,47,85,.35)"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(x - 220, y + 18); ctx.lineTo(x + 220, y + 18); ctx.stroke();
      ctx.fillStyle = MUTED; ctx.font = "600 19px " + SANS; spaced(ctx, label.toUpperCase(), x, y + 50, 2.5);
    }
    var LX = 470, RX = W - 470;
    if (d.signoff) {
      field(LX, 960, d.date, "Date completed");
      // Blank line for a hand signature on the printed copy (about 13 mm of writing space above it).
      ctx.strokeStyle = INK; ctx.lineWidth = 1.6;
      ctx.beginPath(); ctx.moveTo(LX - 250, 1150); ctx.lineTo(LX + 250, 1150); ctx.stroke();
      ctx.fillStyle = MUTED; ctx.font = "600 18px " + SANS; spaced(ctx, "PRECEPTOR SIGNATURE OVER PRINTED NAME", LX, 1178, 1.6);
      ctx.font = "500 18px " + SANS; ctx.fillText("Unit and date signed: ______________________", LX, 1208);
    } else {
      field(LX, 1010, d.date, "Date completed");
    }

    // center seal
    seal(ctx, W / 2, 1052, d.iso.slice(0, 4));

    // bottom right: QR + code, or code only
    var qr = d.verified ? qrMatrix(VERIFY + d.code) : null;
    if (qr) {
      var size = 150, x = RX - size / 2, y = 918, n = qr.length, cell = size / n;
      ctx.fillStyle = "#ffffff"; ctx.fillRect(x - 8, y - 8, size + 16, size + 16);
      ctx.strokeStyle = GOLD; ctx.lineWidth = 2; ctx.strokeRect(x - 8, y - 8, size + 16, size + 16);
      ctx.fillStyle = "#111827";
      for (var r = 0; r < n; r++) for (var c = 0; c < n; c++)
        if (qr[r][c]) ctx.fillRect(Math.floor(x + c * cell), Math.floor(y + r * cell), Math.ceil(cell), Math.ceil(cell));
      ctx.fillStyle = INK; ctx.font = "700 24px " + SANS; ctx.fillText(d.code, RX, 1118);
      ctx.fillStyle = MUTED; ctx.font = "600 19px " + SANS; spaced(ctx, "SCAN TO VERIFY", RX, 1148, 2.5);
    } else {
      field(RX, 990, d.code, "Certificate code");
      ctx.fillStyle = MUTED; ctx.font = "italic 400 20px " + SERIF; ctx.fillText("Not registered for online verification", RX, 1074);
    }

    // fine print
    ctx.fillStyle = MUTED; ctx.font = "400 20px " + SANS;
    wrap(ctx, "Self-study certificate of completion, issued on passing the online end-of-course examination. Not CPD-accredited. " +
      "Competence is demonstrated on the learner's own unit and signed off by a preceptor." +
      (qr ? " Verify at renalcarematters.com/verify." : ""), W / 2, 1252, 1480, 30);
  }

  // QR code (qrcode-generator, MIT, bundled ahead of this script): returns a boolean matrix, quiet zone included.
  function qrMatrix(text) {
    if (typeof qrcode !== "function") return null;
    var q = qrcode(0, "M"); q.addData(text); q.make();
    var n = q.getModuleCount(), pad = 2, m = [];
    for (var r = -pad; r < n + pad; r++) {
      var row = [];
      for (var c = -pad; c < n + pad; c++) row.push(r >= 0 && c >= 0 && r < n && c < n && q.isDark(r, c));
      m.push(row);
    }
    return m;
  }

  /* ---------- UI ---------- */
  var panel = null, modal = null;
  var css = document.createElement("style");
  css.textContent = [
    ".rcm-cert{margin-top:14px;padding:16px 18px;border-radius:12px;border:1px solid #b8892b;background:#fff8e6;color:#1e2a38}",
    ".rcm-cert h3{margin:0;font:800 20px/1.25 Inter,Manrope,sans-serif;color:#1f3864}",
    ".rcm-cert-hd{display:flex;align-items:center;gap:12px;margin-bottom:10px}.rcm-cert-medal{width:54px;height:54px;flex:none;animation:rcmPop .6s cubic-bezier(.2,1.6,.4,1) both}",
    ".rcm-cert-kicker{font:800 12.5px/1 Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#8a6312;margin-bottom:4px}",
    ".rcm-cert{animation:rcmRise .5s ease-out both;box-shadow:0 10px 28px rgba(176,138,46,.22)}",
    "@keyframes rcmPop{0%{transform:scale(.2) rotate(-20deg);opacity:0}100%{transform:none;opacity:1}}",
    "@keyframes rcmRise{0%{transform:translateY(10px);opacity:0}100%{transform:none;opacity:1}}",
    "@media (prefers-reduced-motion:reduce){.rcm-cert,.rcm-cert-medal{animation:none}}",
    ".rcm-confetti{position:fixed;inset:0;width:100vw;height:100vh;pointer-events:none;z-index:2147483001}",
    "html[data-theme='dark'] .rcm-cert-kicker{color:#f3c46a}",
    ".rcm-cert p{text-align:left!important;hyphens:none!important;margin:0 0 10px;font-size:14.5px;line-height:1.55}",
    ".rcm-cert-row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}",
    ".rcm-cert input[type=text]{flex:1 1 240px;min-width:0;font:600 16px Inter,sans-serif;padding:10px 12px;border-radius:10px;border:1px solid #9aa3b2;background:#fff;color:#1e2a38}",
    ".rcm-cert button,.rcm-certm button{font:700 15px Inter,sans-serif;padding:10px 16px;border-radius:999px;border:2px solid #1f3864;background:#1f3864;color:#fff;cursor:pointer}",
    ".rcm-certm button.ghost{background:transparent;color:#1f3864}",
    ".rcm-cert-opt{display:flex;gap:8px;align-items:flex-start;margin-top:10px;font-size:14px;line-height:1.45;cursor:pointer}",
    ".rcm-cert-opt input{width:18px;height:18px;flex:none;margin:1px 0 0;padding:0;accent-color:#1f3864}",
    ".rcm-cert-ts{margin-top:10px}.rcm-cert-ts:empty{display:none}.rcm-cert-msg{margin:10px 0 0!important;font-weight:600}",
    ".rcm-cert button:disabled{opacity:.6;cursor:wait}",
    ".rcm-cert small{display:block;margin-top:8px;color:#5a6678;font-size:12.5px;line-height:1.5}",
    "html[data-theme='dark'] .rcm-cert{background:#2a2414;border-color:#8a6a24;color:#e8e2d4}",
    "html[data-theme='dark'] .rcm-cert button{background:#f3c46a;border-color:#f3c46a;color:#1e2a38}",
    "html[data-theme='dark'] .rcm-cert h3{color:#f3c46a}html[data-theme='dark'] .rcm-cert small{color:#b9b2a2}",
    ".rcm-certm{position:fixed;inset:0;z-index:2147483000;background:rgba(10,18,32,.78);display:flex;align-items:center;justify-content:center;padding:16px}",
    ".rcm-certm-box{background:#fff;border-radius:14px;max-width:980px;width:100%;max-height:100%;overflow:auto;padding:14px;box-shadow:0 20px 50px rgba(0,0,0,.4)}",
    ".rcm-certm img{display:block;width:100%;height:auto;border:1px solid #d6dae1;border-radius:6px}",
    ".rcm-certm-act{display:flex;flex-wrap:wrap;gap:8px;justify-content:flex-end;margin-top:12px}",
    "#rcm-cert-print{display:none}",
    "@media print{html.rcm-cert-printing body>*:not(#rcm-cert-print){display:none!important}",
    "html.rcm-cert-printing #rcm-cert-print{display:block!important}html.rcm-cert-printing #rcm-cert-print img{width:100%;height:auto}",
    "@page{size:A4 landscape;margin:8mm}.rcm-cert{display:none!important}}"
  ].join("\n");
  document.head.appendChild(css);

  // Online registration: GET /api/certs says whether verification is available (and the Turnstile key).
  var cfg = null;
  function config() {
    if (cfg) return cfg;
    cfg = fetch(API, { cache: "no-store" }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; });
    return cfg;
  }
  var tsWidget = null;
  function turnstile(holder, key) {
    if (!key || tsWidget !== null) return;
    tsWidget = -1;
    window.rcmCertTs = function () {
      try { tsWidget = window.turnstile.render(holder, { sitekey: key, size: "flexible", theme: "auto" }); } catch (e) { tsWidget = null; }
    };
    var sc = document.createElement("script");
    sc.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=rcmCertTs";
    sc.async = true; document.head.appendChild(sc);
  }
  function tsToken() {
    try { if (tsWidget !== null && tsWidget !== -1 && window.turnstile) return window.turnstile.getResponse(tsWidget) || ""; } catch (e) {}
    return "";
  }
  var issued = {};   // name|score|total -> {code, issued}, so tapping twice reuses the same certificate

  function register(d) {
    var k = d.name + "|" + d.score + "|" + d.total;
    if (issued[k]) return Promise.resolve(issued[k]);
    return config().then(function (c) {
      if (!c || !c.ready) return null;
      return fetch(API, {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ name: d.name, track: d.track, exam: location.pathname.split("/").pop().replace(/\.html$/, ""),
          modules: d.modules, score: d.score, total: d.total, exam_min: d.examMin, study_min: d.studyMin,
          turnstile: tsToken(), website: "" })
      }).then(function (r) { return r.json().then(function (j) { return r.ok ? j : { error: j.error || "server" }; }); });
    }).then(function (j) {
      if (j && j.code) issued[k] = j;
      return j;
    }, function () { return null; });
  }

  function isoText(iso) {
    var p = iso.split("-");
    return MONTHS[+p[1] - 1] + " " + +p[2] + ", " + p[0];
  }

  function showPanel(p) {
    if (panel) panel.remove();
    panel = document.createElement("div");
    panel.className = "rcm-cert";
    panel.innerHTML =
      '<div class="rcm-cert-hd">' + MEDAL + '<div><div class="rcm-cert-kicker">Congratulations!</div>' +
      '<h3>You passed the ' + esc(trackName()) + ' course</h3></div></div>' +
      '<p>' + p.score + ' of ' + p.total + ' best answers (' + Math.round(100 * p.score / p.total) + '%)' +
      (p.score / p.total >= DISTINCTION ? ', <strong>with distinction</strong>' : '') + '. You have earned your certificate of completion. ' +
      'Type your name the way you want it printed, then tap <strong>Make my certificate</strong>.</p>' +
      '<div class="rcm-cert-row"><input type="text" maxlength="70" autocomplete="name" placeholder="Full name, e.g. Juan Dela Cruz" aria-label="Name to print on the certificate">' +
      '<button type="button">Make my certificate</button></div>' +
      '<label class="rcm-cert-opt"><input type="checkbox"> Add a preceptor sign-off line (optional; signed by hand on the printed copy)</label>' +
      '<div class="rcm-cert-ts"></div>' +
      '<p class="rcm-cert-msg" role="status" hidden></p>' +
      '<small>To make the certificate verifiable, your name, the track, the date and your score are saved with its code on ' +
      'renalcarematters.com; anyone who scans its QR code sees them. To have your record removed, use Report a correction ' +
      'on any guide. This is a self-study certificate, not CPD units.</small>';
    result.appendChild(panel);
    celebrate(panel);
    var input = panel.querySelector("input"), btn = panel.querySelector("button"), msg = panel.querySelector(".rcm-cert-msg");
    config().then(function (c) { if (c && c.turnstile) turnstile(panel.querySelector(".rcm-cert-ts"), c.turnstile); });
    function say(t) { msg.textContent = t; msg.hidden = !t; }
    function go() {
      var name = input.value.replace(/\s+/g, " ").trim();
      if (name.length < 2) { input.focus(); input.setAttribute("aria-invalid", "true"); return; }
      input.removeAttribute("aria-invalid");
      btn.disabled = true; say("Making your certificate…");
      var t = today(), track = trackName();
      var d = { name: name, track: track, modules: moduleCount(), score: p.score, total: p.total,
                studyMin: STUDY_MIN, examMin: examMin, date: t.text, iso: t.iso,
                signoff: panel.querySelector(".rcm-cert-opt input").checked };
      register(d).then(function (j) {
        btn.disabled = false;
        if (j && j.code) {
          say(""); d.code = j.code; d.verified = true; d.date = isoText(j.issued); openCert(d); return;
        }
        if (j && j.error === "human_check") { say("Please complete the human check above, then tap Make my certificate again."); return; }
        if (j && j.error === "limit") say("Too many certificates from this connection today, so this copy is not registered for verification.");
        else say("Could not reach the site to register the certificate, so this copy has no QR code. Connect to the internet and tap again for a verifiable one.");
        code(name, track, t.iso, p.score, p.total).then(function (c) { d.code = c; d.verified = false; openCert(d); });
      });
    }
    btn.addEventListener("click", go);
    input.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); go(); } });
  }

  function openCert(d) {
    var canvas = document.createElement("canvas");
    var ready = document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve();
    ready.then(function () {
      draw(canvas, d);
      var url = canvas.toDataURL("image/png");
      var file = "Certificate-" + d.track.replace(/[^A-Za-z0-9]+/g, "-") + "-" + d.name.replace(/[^A-Za-z0-9]+/g, "-") + ".png";
      if (modal) modal.remove();
      modal = document.createElement("div");
      modal.className = "rcm-certm";
      modal.setAttribute("role", "dialog"); modal.setAttribute("aria-modal", "true"); modal.setAttribute("aria-label", "Your certificate");
      modal.innerHTML = '<div class="rcm-certm-box"><img alt=""><div class="rcm-certm-act">' +
        '<button type="button" data-a="save">Save image</button>' +
        '<button type="button" data-a="print">Print or save as PDF</button>' +
        '<button type="button" class="ghost" data-a="close">Close</button></div></div>';
      var img = modal.querySelector("img");
      img.src = url; img.alt = "Certificate of completion for " + d.name + ", " + d.track + ", " + d.date + ", code " + d.code;
      document.body.appendChild(modal);
      modal.querySelector('[data-a="save"]').focus();
      modal.addEventListener("click", function (e) {
        var a = e.target.closest("[data-a]"); if (e.target === modal) a = { getAttribute: function () { return "close"; } };
        if (!a) return;
        var act = a.getAttribute("data-a");
        if (act === "close") { modal.remove(); modal = null; }
        else if (act === "save") save(canvas, url, file);
        else if (act === "print") printCert(url);
      });
      document.addEventListener("keydown", function esc(e) {
        if (e.key === "Escape" && modal) { modal.remove(); modal = null; document.removeEventListener("keydown", esc); }
      });
    });
  }

  function save(canvas, url, file) {
    // Phones: the share sheet lets the learner save to Photos or Files; elsewhere a normal download.
    if (canvas.toBlob && navigator.canShare && window.File) {
      canvas.toBlob(function (blob) {
        var f = new File([blob], file, { type: "image/png" });
        if (navigator.canShare({ files: [f] })) {
          navigator.share({ files: [f], title: "Certificate of completion" }).catch(function () {});
        } else download(url, file);
      }, "image/png");
    } else download(url, file);
  }
  function download(url, file) {
    var a = document.createElement("a"); a.href = url; a.download = file;
    document.body.appendChild(a); a.click(); a.remove();
  }
  function printCert(url) {
    var holder = document.getElementById("rcm-cert-print");
    if (!holder) { holder = document.createElement("div"); holder.id = "rcm-cert-print"; document.body.appendChild(holder); }
    holder.innerHTML = '<img alt="Certificate of completion">';
    var img = holder.querySelector("img");
    img.onload = function () {
      document.documentElement.classList.add("rcm-cert-printing");
      setTimeout(function () { window.print(); }, 50);
    };
    img.src = url;
  }
  window.addEventListener("afterprint", function () { document.documentElement.classList.remove("rcm-cert-printing"); });

  /* Watch the examination result: offer the certificate after a pass, remove it when a new set is drawn. */
  var busy = false;
  new MutationObserver(function () {
    if (busy) return;
    if (panel && !result.contains(panel)) panel = null;
    var p = passed();
    if (p && !panel) { busy = true; showPanel(p); busy = false; }
    else if (!p && panel) { panel.remove(); panel = null; }
  }).observe(result, { childList: true, characterData: true, subtree: true });
})();
