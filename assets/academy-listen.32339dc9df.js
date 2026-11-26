/*! easy-speech 2.4.0 | MIT License | (c) 2021 Jan Küster | https://github.com/leaonline/easy-speech
 * Cross-browser wrapper for the Web Speech API (speechSynthesis). Vendored unmodified for the Academy Listen player. */
var EasySpeech = (function () {
  'use strict';

  function _iterableToArrayLimit(r, l) {
    var t = null == r ? null : "undefined" != typeof Symbol && r[Symbol.iterator] || r["@@iterator"];
    if (null != t) {
      var e,
        n,
        i,
        u,
        a = [],
        f = !0,
        o = !1;
      try {
        if (i = (t = t.call(r)).next, 0 === l) {
          if (Object(t) !== t) return;
          f = !1;
        } else for (; !(f = (e = i.call(t)).done) && (a.push(e.value), a.length !== l); f = !0);
      } catch (r) {
        o = !0, n = r;
      } finally {
        try {
          if (!f && null != t.return && (u = t.return(), Object(u) !== u)) return;
        } finally {
          if (o) throw n;
        }
      }
      return a;
    }
  }
  function ownKeys(e, r) {
    var t = Object.keys(e);
    if (Object.getOwnPropertySymbols) {
      var o = Object.getOwnPropertySymbols(e);
      r && (o = o.filter(function (r) {
        return Object.getOwnPropertyDescriptor(e, r).enumerable;
      })), t.push.apply(t, o);
    }
    return t;
  }
  function _objectSpread2(e) {
    for (var r = 1; r < arguments.length; r++) {
      var t = null != arguments[r] ? arguments[r] : {};
      r % 2 ? ownKeys(Object(t), !0).forEach(function (r) {
        _defineProperty(e, r, t[r]);
      }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : ownKeys(Object(t)).forEach(function (r) {
        Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r));
      });
    }
    return e;
  }
  function _defineProperty(obj, key, value) {
    key = _toPropertyKey(key);
    if (key in obj) {
      Object.defineProperty(obj, key, {
        value: value,
        enumerable: true,
        configurable: true,
        writable: true
      });
    } else {
      obj[key] = value;
    }
    return obj;
  }
  function _objectWithoutPropertiesLoose(source, excluded) {
    if (source == null) return {};
    var target = {};
    var sourceKeys = Object.keys(source);
    var key, i;
    for (i = 0; i < sourceKeys.length; i++) {
      key = sourceKeys[i];
      if (excluded.indexOf(key) >= 0) continue;
      target[key] = source[key];
    }
    return target;
  }
  function _objectWithoutProperties(source, excluded) {
    if (source == null) return {};
    var target = _objectWithoutPropertiesLoose(source, excluded);
    var key, i;
    if (Object.getOwnPropertySymbols) {
      var sourceSymbolKeys = Object.getOwnPropertySymbols(source);
      for (i = 0; i < sourceSymbolKeys.length; i++) {
        key = sourceSymbolKeys[i];
        if (excluded.indexOf(key) >= 0) continue;
        if (!Object.prototype.propertyIsEnumerable.call(source, key)) continue;
        target[key] = source[key];
      }
    }
    return target;
  }
  function _slicedToArray(arr, i) {
    return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _unsupportedIterableToArray(arr, i) || _nonIterableRest();
  }
  function _arrayWithHoles(arr) {
    if (Array.isArray(arr)) return arr;
  }
  function _unsupportedIterableToArray(o, minLen) {
    if (!o) return;
    if (typeof o === "string") return _arrayLikeToArray(o, minLen);
    var n = Object.prototype.toString.call(o).slice(8, -1);
    if (n === "Object" && o.constructor) n = o.constructor.name;
    if (n === "Map" || n === "Set") return Array.from(o);
    if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen);
  }
  function _arrayLikeToArray(arr, len) {
    if (len == null || len > arr.length) len = arr.length;
    for (var i = 0, arr2 = new Array(len); i < len; i++) arr2[i] = arr[i];
    return arr2;
  }
  function _nonIterableRest() {
    throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
  }
  function _toPrimitive(input, hint) {
    if (typeof input !== "object" || input === null) return input;
    var prim = input[Symbol.toPrimitive];
    if (prim !== undefined) {
      var res = prim.call(input, hint || "default");
      if (typeof res !== "object") return res;
      throw new TypeError("@@toPrimitive must return a primitive value.");
    }
    return (hint === "string" ? String : Number)(input);
  }
  function _toPropertyKey(arg) {
    var key = _toPrimitive(arg, "string");
    return typeof key === "symbol" ? key : String(key);
  }

  var _excluded = ["text", "voice", "pitch", "rate", "volume", "force", "infiniteResume", "noStop"];
  /**
   * @module EasySpeech
   * @typicalname EasySpeech
   */

  /**
   * Cross browser Speech Synthesis with easy API.
   * This project was created, because it's always a struggle to get the synthesis
   * part of `Web Speech API` running on most major browsers.
   *
   * Setup is very straight forward (see example).
   *
   * @example
   * import EasySpeech from 'easy-speech'
   *
   * const example = async () => {
   *   await EasySpeech.init() // required
   *   await EasySpeech.speak({ 'Hello, world' })
   * }
   *
   * @see https://wicg.github.io/speech-api/#tts-section
   * @see https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis
   * @type {Object}
   */
  var EasySpeech = {};

  /**
   * To support multiple environments (browser, node) we define scope, based
   * on what's available with window as priority, since Browsers are main target.
   * @private
   */
  var scope = typeof globalThis === 'undefined' ? window : globalThis;

  /**
   * @private
   * @type {{
   *  status: String,
      initialized: Boolean,
      speechSynthesis: null|SpeechSynthesis,
      speechSynthesisUtterance: null|SpeechSynthesisUtterance,
      speechSynthesisVoice: null|SpeechSynthesisVoice,
      speechSynthesisEvent: null|SpeechSynthesisEvent,
      speechSynthesisErrorEvent: null|SpeechSynthesisErrorEvent,
      voices: null|Array<SpeechSynthesisVoice>,
      maxLengthExceeded: string,
      defaults: {
        pitch: Number,
        rate: Number,
        volume: Number,
        voice: null|SpeechSynthesisVoice
      },
      handlers: {}
   * }}
   */
  var internal = {
    status: 'created'
  };
  var patches = {};

  /*******************************************************************************
   *
   * AVAILABLE WITHOUT INIT
   *
   ******************************************************************************/

  /**
   * Enable module-internal debugging by passing your own callback function.
   * Debug will automatically pass through all updates to `status`
   *
   * @example
   * import EasySpeech from 'easy-speech'
   * import Log from '/path/to/my/Log'
   *
   * EasySpeech.debug(arg => Log.debug('EasySpeech:', arg))
   *
   * @param {Function} fn A function, which always receives one argument, that
   *  represents a current debug message
   */
  EasySpeech.debug = function (fn) {
    debug = typeof fn === 'function' ? fn : function () {};
  };
  var debug = function debug() {};

  /**
   * Detects all possible occurrences of the main Web Speech API components
   * in the global scope.
   *
   * The returning object will have the following structure (see example).
   *
   * @example
   * EasySpeech.detect()
   *
   * {
   *     speechSynthesis: SpeechSynthesis|undefined,
   *     speechSynthesisUtterance: SpeechSynthesisUtterance|undefined,
   *     speechSynthesisVoice: SpeechSynthesisVoice|undefined,
   *     speechSynthesisEvent: SpeechSynthesisEvent|undefined,
   *     speechSynthesisErrorEvent: SpeechSynthesisErrorEvent|undefined,
   *     onvoiceschanged: Boolean,
   *     onboundary: Boolean,
   *     onend: Boolean,
   *     onerror: Boolean,
   *     onmark: Boolean,
   *     onpause: Boolean,
   *     onresume: Boolean,
   *     onstart: Boolean
   * }
   *
   * @returns {object} An object containing all possible features and their status
   */
  EasySpeech.detect = function () {
    return detectFeatures();
  };

  /** @private **/
  var detectFeatures = function detectFeatures() {
    var features = {};
    ['speechSynthesis', 'speechSynthesisUtterance', 'speechSynthesisVoice', 'speechSynthesisEvent', 'speechSynthesisErrorEvent'].forEach(function (feature) {
      features[feature] = detect(feature);
    });
    features.onvoiceschanged = hasProperty(features.speechSynthesis, 'onvoiceschanged');
    var hasUtterance = hasProperty(features.speechSynthesisUtterance, 'prototype');
    utteranceEvents.forEach(function (event) {
      var name = "on".concat(event);
      features[name] = hasUtterance && hasProperty(features.speechSynthesisUtterance.prototype, name);
    });

    // not published to the outside
    patches.isAndroid = isAndroid();
    patches.isFirefox = isFirefox() || isKaiOS();
    patches.isSafari = isSafari();
    debug("is android: ".concat(!!patches.isAndroid));
    debug("is firefox: ".concat(!!patches.isFirefox));
    debug("is safari: ".concat(!!patches.isSafari));
    return features;
  };

  /** @private **/
  var hasProperty = function hasProperty() {
    var target = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
    var prop = arguments.length > 1 ? arguments[1] : undefined;
    return Object.hasOwnProperty.call(target, prop) || prop in target || !!target[prop];
  };

  /** @private **/
  var getUA = function getUA() {
    return (scope.navigator || {}).userAgent || '';
  };

  /** @private **/
  var isAndroid = function isAndroid() {
    return /android/i.test(getUA());
  };

  /** @private **/
  var isKaiOS = function isKaiOS() {
    return /kaios/i.test(getUA());
  };

  /** @private **/
  var isFirefox = function isFirefox() {
    // InstallTrigger will soon be deprecated
    if (typeof scope.InstallTrigger !== 'undefined') {
      return true;
    }
    return /firefox/i.test(getUA());
  };

  /** @private **/
  var isSafari = function isSafari() {
    return typeof scope.GestureEvent !== 'undefined';
  };

  /**
   * Common prefixes for browsers that tend to implement their custom names for
   * certain parts of their API.
   * @private
   **/
  var prefixes = ['webKit', 'moz', 'ms', 'o'];

  /**
   * Make the first character of a String uppercase
   * @private
   **/
  var capital = function capital(s) {
    return "".concat(s.charAt(0).toUpperCase()).concat(s.slice(1));
  };

  /**
   * Find a feature in global scope by checking for various combinations and
   * variations of the base-name
   * @param {String} baseName name of the component to look for, must begin with
   *   lowercase char
   * @return {Object|undefined} The component from global scope, if found
   * @private
   **/
  var detect = function detect(baseName) {
    var capitalBaseName = capital(baseName);
    var baseNameWithPrefixes = prefixes.map(function (p) {
      return "".concat(p).concat(capitalBaseName);
    });
    var found = [baseName, capitalBaseName].concat(baseNameWithPrefixes).find(inGlobalScope);
    return scope[found];
  };

  /**
   * Returns, if a given name exists in global scope
   * @private
   * @param name
   * @return {boolean}
   */
  var inGlobalScope = function inGlobalScope(name) {
    return scope[name];
  };

  /**
   * Returns a shallow copy of the current internal status. Depending of the
   * current state this might return an object with only a single field `status`
   * or a complete Object, including detected features, `defaults`, `handlers`
   * and supported `voices`.
   *
   * @example
   * import EasySpeech from 'easy-speech'
   *
   * // uninitialized
   * EasySpeech.status() // { status: 'created' }
   *
   * // after EasySpeech.init
   * EasySpeech.status()
   *
   * {
   *   status: 'init: complete',
   *   initialized: true,
   *   speechSynthesis: speechSynthesis,
   *   speechSynthesisUtterance: SpeechSynthesisUtterance,
   *   speechSynthesisVoice: SpeechSynthesisVoice,
   *   speechSynthesisEvent: SpeechSynthesisEvent,
   *   speechSynthesisErrorEvent: SpeechSynthesisErrorEvent,
   *   voices: [...],
   *   defaults: {
   *     pitch: 1,
   *     rate: 1,
   *     volume: 1,
   *     voice: null
   *   },
   *   handlers: {}
   * }
   *
   * @return {Object} the internal status
   */
  EasySpeech.status = function () {
    return _objectSpread2({}, internal);
  };

  /**
   * Returns a filtered subset of available voices by given
   * parameters. Multiple parameters can be used.
   * @param name {string=} a string that is expected to occur in the voices name; does not need to be the full name
   * @param voiceURI {string=} a string that is expected to occur in the voices voiceURI; does not need to be the full URI
   * @param language {string=} a language code to filter by .lang; short and long-form are accepted
   * @param localService {boolean=} use true/false to include/exclude local/remote voices
   * @return {SpeechSynthesisVoice[]} a list of voices, matching the given rules
   */
  EasySpeech.filterVoices = function (_ref) {
    var name = _ref.name,
      language = _ref.language,
      localService = _ref.localService,
      voiceURI = _ref.voiceURI;
    var voices = internal.voices || [];
    var hasName = typeof name !== 'undefined';
    var hasVoiceURI = typeof voiceURI !== 'undefined';
    var hasLocalService = typeof localService !== 'undefined';
    var hasLang = typeof language !== 'undefined';
    var langCode = hasLang && language.split(/[-_]+/g)[0].toLocaleLowerCase();
    return voices.filter(function (v) {
      if (hasName && v.name.includes(name) || hasVoiceURI && v.voiceURI.includes(voiceURI) || hasLocalService && v.localService === localService) {
        return true;
      }
      if (hasLang) {
        var compareLang = v.lang && v.lang.toLocaleLowerCase();
        return compareLang && (compareLang === langCode || compareLang.indexOf("".concat(langCode, "-")) > -1 || compareLang.indexOf("".concat(langCode, "_")) > -1);
      }
      return false;
    });
  };

  /**
   * Updates the internal status
   * @private
   * @param {String} s the current status to set
   */
  var status = function status(s) {
    debug(s);
    internal.status = s;
  };

  /**
   * This is the function you need to run, before being able to speak.
   * It includes:
   * - feature detection
   * - feature assignment (into internal state)
   * - voices loading
   * - state update
   * - inform caller about success
   *
   * It will load voices by a variety of strategies:
   *
   * - detect and that SpeechSynthesis is basically supported, if not -> fail
   * - load voices directly
   * - if not loaded but `onvoiceschanged` is available: use `onvoiceschanged`
   * - if `onvoiceschanged` is not available: fallback to timeout
   * - if `onvoiceschanged` is fired but no voices available: fallback to timeout
   * - timeout reloads voices in a given `interval` until a `maxTimeout` is reached
   * - if voices are loaded until then -> complete
   * - if no voices found -> fail
   *
   * Note: if once initialized you can't re-init (will skip and resolve to
   * `false`) unless you run `EasySpeech.reset()`.
   *
   * @param maxTimeout {number}[5000] the maximum timeout to wait for voices in ms
   * @param interval {number}[250] the interval in ms to check for voices
   * @param quiet {boolean=} prevent rejection on errors, e.g. if no voices
   * @param maxLengthExceeded {string=} defines what to do, if max text length (4096 bytes) is exceeded:
   * - 'error' - throw an Error
   * - 'none' - do nothing; note that some voices may not speak the text at all without any error or warning
   * - 'warn' - default, raises a warning
   * @return {Promise<Boolean>}
   * @fulfil {Boolean} true, if initialized, false, if skipped (because already
   *   initialized)
   * @reject {Error} - The error `message` property will always begin with
   *   `EasySpeech: ` and contain one of the following:
   *
   *   - `browser misses features` - The browser will not be able to use speech
   *      synthesis at all as it misses crucial features
   *   - `browser has no voices (timeout)` - No voice could be loaded with neither
   *      of the given strategies; chances are high the browser does not have
   *      any voices embedded (example: Chromium on *buntu os')
   */

  EasySpeech.init = function () {
    var _ref2 = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {},
      _ref2$maxTimeout = _ref2.maxTimeout,
      maxTimeout = _ref2$maxTimeout === void 0 ? 5000 : _ref2$maxTimeout,
      _ref2$interval = _ref2.interval,
      interval = _ref2$interval === void 0 ? 250 : _ref2$interval,
      quiet = _ref2.quiet,
      maxLengthExceeded = _ref2.maxLengthExceeded;
    return new Promise(function (resolve, reject) {
      if (internal.initialized) {
        return resolve(false);
      }
      EasySpeech.reset();
      status('init: start');

      // there may be the case, that the browser needs to load using a timer
      // so we declare it at the top to make sure the interval is always cleared
      // when we exit the Promise via fail / complete
      var timer;
      var voicesChangedListener;
      var completeCalled = false;
      internal.maxLengthExceeded = maxLengthExceeded || 'warn';
      var fail = function fail(errorMessage) {
        status("init: failed (".concat(errorMessage, ")"));
        clearInterval(timer);
        internal.initialized = false;

        // we have the option to fail quiet here
        return quiet ? resolve(false) : reject(new Error("EasySpeech: ".concat(errorMessage)));
      };
      var complete = function complete() {
        // avoid race-conditions between listeners and timeout
        if (completeCalled) {
          return;
        }
        status('init: complete');

        // set flags immediately
        completeCalled = true;
        internal.initialized = true;

        // cleanup events and timer
        clearInterval(timer);
        speechSynthesis.onvoiceschanged = null;
        if (voicesChangedListener) {
          speechSynthesis.removeEventListener('voiceschanged', voicesChangedListener);
        }

        // all done
        return resolve(true);
      };

      // before initializing we force-detect all required browser features
      var features = detectFeatures();
      var hasAllFeatures = !!features.speechSynthesis && !!features.speechSynthesisUtterance;
      if (!hasAllFeatures) {
        return fail('browser misses features');
      }

      // assign all detected features to our internal definitions
      Object.keys(features).forEach(function (feature) {
        internal[feature] = features[feature];
      });

      // start initializing
      var speechSynthesis = internal.speechSynthesis;
      var voicesLoaded = function voicesLoaded() {
        var voices = speechSynthesis.getVoices() || [];
        if (voices.length > 0) {
          internal.voices = voices;
          status("voices loaded: ".concat(voices.length));

          // if we find a default voice, set it as default
          internal.defaultVoice = voices.find(function (v) {
            return v["default"];
          });

          // otherwise let's stick to the first one we can find by locale
          if (!internal.defaultVoice) {
            var language = (scope.navigator || {}).language || '';
            var filtered = EasySpeech.filterVoices({
              language: language
            });
            if (filtered.length > 0) {
              internal.defaultVoice = filtered[0];
            }
          }

          // otherwise let's use the first element in the array
          if (!internal.defaultVoice) {
            internal.defaultVoice = voices[0];
          }
          return true;
        }
        return false;
      };
      status('init: voices');

      // best case: detect if voices can be loaded directly
      if (voicesLoaded()) {
        return complete();
      }

      // last possible fallback method: run a timer until max. timeout and reload
      var loadViaTimeout = function loadViaTimeout() {
        status('init: voices (timer)');
        var timeout = 0;
        timer = setInterval(function () {
          if (voicesLoaded()) {
            return complete();
          }
          if (timeout > maxTimeout) {
            return fail('browser has no voices (timeout)');
          }
          timeout += interval;
        }, interval);
      };

      // detect if voices can be loaded after onveoiceschanged,
      // but only if the browser supports this event
      if (features.onvoiceschanged) {
        status('init: voices (onvoiceschanged)');
        speechSynthesis.onvoiceschanged = function () {
          if (voicesLoaded()) {
            return complete();
          }

          // xxx: some browsers (like chrome on android still have not all
          // voices loaded at this point, whichs is why we need to enter
          // the timeout-based method here.
          return loadViaTimeout();
        };

        // xxx: there is an edge-case where browser provide onvoiceschanged,
        // but they never load the voices, so init would never complete
        // in such case we need to fail after maxTimeout
        setTimeout(function () {
          if (voicesLoaded()) {
            return complete();
          }
          return fail('browser has no voices (timeout)');
        }, maxTimeout);
      } else {
        // this is a very problematic case, since we don't really know, whether
        // this event will fire at all, so we need to setup both a listener AND
        // run the timeout and make sure on of them "wins"
        // affected browsers may be: MacOS Safari
        if (hasProperty(speechSynthesis, 'addEventListener')) {
          status('init: voices (addEventListener)');
          voicesChangedListener = function voicesChangedListener() {
            if (voicesLoaded()) {
              return complete();
            }
          };
          speechSynthesis.addEventListener('voiceschanged', voicesChangedListener);
        }

        // for all browser not supporting onveoiceschanged we start a timer
        // until we reach a certain timeout and try to get the voices
        loadViaTimeout();
      }
    });
  };

  /**
   * Placed as first line in functions that require `EasySpeech.init` before they
   * can run.
   * @param {boolean=} force set to true to force-skip check
   * @private
   */
  var ensureInit = function ensureInit() {
    var _ref3 = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {},
      force = _ref3.force;
    if (!force && !internal.initialized) {
      throw new Error('EasySpeech: not initialized. Run EasySpeech.init() first');
    }
  };

  /*******************************************************************************
   *
   * AVAILABLE ONLY AFTER INIT
   *
   ******************************************************************************/

  /**
   * Returns all available voices.
   *
   * @condition `EasySpeech.init` must have been called and resolved to `true`
   * @return {Array<SpeechSynthesisVoice>}
   */
  EasySpeech.voices = function () {
    ensureInit();
    return internal.voices;
  };

  /**
   * Attaches global/default handlers to every utterance instance. The handlers
   * will run in parallel to any additional handlers, attached when calling
   * `EasySpeech.speak`
   *
   * @condition `EasySpeech.init` must have been called and resolved to `true`
   *
   * @param {Object} handlers
   * @param {function=} handlers.boundary - optional, event handler
   * @param {function=} handlers.end - optional, event handler
   * @param {function=} handlers.error - optional, event handler
   * @param {function=} handlers.mark - optional, event handler
   * @param {function=} handlers.pause - optional, event handler
   * @param {function=} handlers.resume - optional, event handler
   * @param {function=} handlers.start - optional, event handler
   *
   * @return {Object} a shallow copy of the Object, containing all global handlers
   */
  EasySpeech.on = function (handlers) {
    ensureInit();
    utteranceEvents.forEach(function (name) {
      var handler = handlers[name];
      if (validate.handler(handler)) {
        internal.handlers[name] = handler;
      }
    });
    return _objectSpread2({}, internal.handlers);
  };

  /**
   * We use these keys to search for these events in handler objects and defaults
   * @private
   */
  var utteranceEvents = ['boundary', 'end', 'error', 'mark', 'pause', 'resume', 'start'];

  /**
   * Internal validation of passed parameters
   * @private
   */
  var validate = {
    isNumber: function isNumber(n) {
      return typeof n === 'number' && !Number.isNaN(n);
    },
    pitch: function pitch(p) {
      return validate.isNumber(p) && p >= 0 && p <= 2;
    },
    volume: function volume(v) {
      return validate.isNumber(v) && v >= 0 && v <= 1;
    },
    rate: function rate(r) {
      return validate.isNumber(r) && r >= 0.1 && r <= 10;
    },
    text: function text(t) {
      return typeof t === 'string';
    },
    handler: function handler(h) {
      return typeof h === 'function';
    },
    // we prefer duck typing here, mostly because there are cases where
    // SpeechSynthesisVoice is not defined on global scope but is supported
    // when using getVoices().
    voice: function voice(v) {
      return v && v.lang && v.name && v.voiceURI;
    }
  };

  /**
   * Sets defaults for utterances. Invalid values will be ignored without error
   * or warning.
   *
   * @see https://wicg.github.io/speech-api/#utterance-attributes
   * @param {object=} options - Optional object containing values to set values
   * @param {object=} options.voice - Optional `SpeechSynthesisVoice` instance or
   *  `SpeechSynthesisVoice`-like Object
   * @param {number=} options.pitch - Optional pitch value >= 0 and <= 2
   * @param {number=} options.rate - Optional rate value >= 0.1 and <= 10
   * @param {number=} options.volume - Optional volume value >= 0 and <= 1
   *
   * @return {object} a shallow copy of the current defaults
   */
  EasySpeech.defaults = function (options) {
    ensureInit();
    if (options) {
      internal.defaults = internal.defaults || {};
      ['voice', 'pitch', 'rate', 'volume'].forEach(function (name) {
        var value = options[name];
        var isValid = validate[name];
        if (isValid(value)) {
          internal.defaults[name] = value;
        }
      });
    }
    return _objectSpread2({}, internal.defaults);
  };

  /**
   * Determines the current voice and makes sure, there is always a voice returned
   * @private
   * @param voice
   * @return {*|SpeechSynthesisVoice|{}}
   */
  var getCurrentVoice = function getCurrentVoice(voice) {
    var _internal$defaults, _internal$voices;
    return voice || ((_internal$defaults = internal.defaults) === null || _internal$defaults === void 0 ? void 0 : _internal$defaults.voice) || internal.defaultVoice || ((_internal$voices = internal.voices) === null || _internal$voices === void 0 ? void 0 : _internal$voices[0]);
  };

  /**
   * Creates a new `SpeechSynthesisUtterance` instance
   * @private
   * @param text
   */
  var createUtterance = function createUtterance(text) {
    var UtteranceClass = internal.speechSynthesisUtterance;
    return new UtteranceClass(text);
  };

  /**
   * Speaks a voice by given parameters, constructs utterance by best possible
   * combinations of parameters and defaults.
   *
   * If the given utterance parameters are missing or invalid, defaults will be
   * used as fallback.
   *
   * @example
   * const voice = EasySpeech.voices()[10] // get a voice you like
   *
   * EasySpeech.speak({
   *   text: 'Hello, world',
   *   voice: voice,
   *   pitch: 1.2,  // a little bit higher
   *   rate: 1.7, // a little bit faster
   *   boundary: event => console.debug('word boundary reached', event.charIndex),
   *   error: e => notify(e)
   * })
   *
   * @param {object} options - required options
   * @param {string} text - required text to speak
   * @param {object=} voice - optional `SpeechSynthesisVoice` instance or
   *   structural similar object (if `SpeechSynthesisUtterance` is not supported)
   * @param {number=} options.pitch - Optional pitch value >= 0 and <= 2
   * @param {number=} options.rate - Optional rate value >= 0.1 and <= 10
   * @param {number=} options.volume - Optional volume value >= 0 and <= 1
   * @param {boolean=} options.force - Optional set to true to force speaking, no matter the internal state
   * @param {boolean=} options.infiniteResume - Optional, force or prevent internal resumeInfinity pattern
   * @param {boolean=} options.noStop - Optional, if true will not stop current voices
   * @param {object=} handlers - optional additional local handlers, can be
   *   directly added as top-level properties of the options
   * @param {function=} handlers.boundary - optional, event handler
   * @param {function=} handlers.end - optional, event handler
   * @param {function=} handlers.error - optional, event handler
   * @param {function=} handlers.mark - optional, event handler
   * @param {function=} handlers.pause - optional, event handler
   * @param {function=} handlers.resume - optional, event handler
   * @param {function=} handlers.start - optional, event handler
   *
   * @return {Promise<SpeechSynthesisEvent|SpeechSynthesisErrorEvent>}
   * @fulfill {SpeechSynthesisEvent} Resolves to the `end` event
   * @reject {SpeechSynthesisEvent} rejects using the `error` event
   */
  EasySpeech.speak = function (_ref4) {
    var text = _ref4.text,
      voice = _ref4.voice,
      pitch = _ref4.pitch,
      rate = _ref4.rate,
      volume = _ref4.volume,
      force = _ref4.force,
      infiniteResume = _ref4.infiniteResume,
      noStop = _ref4.noStop,
      handlers = _objectWithoutProperties(_ref4, _excluded);
    ensureInit({
      force: force
    });
    if (!validate.text(text)) {
      throw new Error('EasySpeech: at least some valid text is required to speak');
    }
    if (new TextEncoder().encode(text).length > 4096) {
      var message = 'EasySpeech: text exceeds max length of 4096 bytes, which will not work with some voices.';
      switch (internal.maxLengthExceeded) {
        case 'none':
          break;
        case 'error':
          throw new Error(message);
        case 'warn':
        default:
          console.warn(message);
      }
    }
    var getValue = function getValue(options) {
      var _internal$defaults2;
      var _Object$entries$ = _slicedToArray(Object.entries(options)[0], 2),
        name = _Object$entries$[0],
        value = _Object$entries$[1];
      if (validate[name](value)) {
        return value;
      }
      return (_internal$defaults2 = internal.defaults) === null || _internal$defaults2 === void 0 ? void 0 : _internal$defaults2[name];
    };
    return new Promise(function (resolve, reject) {
      status('init speak');
      var utterance = createUtterance(text);
      var currentVoice = getCurrentVoice(voice);

      // XXX: if we force-speak, we may not get a current voice!
      // This may occur when the browser won't load voices but
      // provides SpeechSynth and SpeechSynthUtterance.
      // We then might at least try to speak something with defaults
      if (currentVoice) {
        utterance.voice = currentVoice;
        utterance.lang = currentVoice.lang;
        utterance.voiceURI = currentVoice.voiceURI;
      }
      utterance.text = text;
      utterance.pitch = getValue({
        pitch: pitch
      });
      utterance.rate = getValue({
        rate: rate
      });
      utterance.volume = getValue({
        volume: volume
      });
      var isMsNatural = utterance.voice && utterance.voice.name && utterance.voice.name.toLocaleLowerCase().includes('(natural)');
      debugUtterance(utterance, {
        isMsNatural: isMsNatural
      });
      utteranceEvents.forEach(function (name) {
        var _internal$handlers;
        var fn = handlers[name];
        if (validate.handler(fn)) {
          utterance.addEventListener(name, fn);
        }
        if ((_internal$handlers = internal.handlers) !== null && _internal$handlers !== void 0 && _internal$handlers[name]) {
          utterance.addEventListener(name, internal.handlers[name]);
        }
      });

      // always attached are start, end and error listeners

      // XXX: chrome won't play longer tts texts in one piece and stops after a few
      // words. We need to add an intervall here in order prevent this. See:
      // https://stackoverflow.com/questions/21947730/chrome-speech-synthesis-with-longer-texts
      //
      // XXX: this apparently works only on chrome desktop, while it breaks chrome
      // mobile (android), so we need to detect chrome desktop
      //
      // XXX: resumeInfinity breaks on firefox macOs so we need to avoid it there
      // as well. Since we don't need it in FF anyway, we can safely skip there
      //
      // XXX: resumeInfinity is also incompatible with older safari ios versions
      // so we skip it on safari, too.
      //
      // XXX: we can force-enable or force-disable infiniteResume via flag now and
      // use the deterministic approach if it's not a boolean value
      utterance.addEventListener('start', function () {
        patches.paused = false;
        patches.speaking = true;
        var defaultResumeInfinity = !isMsNatural && !patches.isFirefox && !patches.isSafari && patches.isAndroid !== true;
        var useResumeInfinity = typeof infiniteResume === 'boolean' ? infiniteResume : defaultResumeInfinity;
        if (useResumeInfinity) {
          resumeInfinity(utterance);
        }
      });
      utterance.addEventListener('end', function (endEvent) {
        status('speak complete');
        patches.paused = false;
        patches.speaking = false;
        clearTimeout(timeoutResumeInfinity);
        resolve(endEvent);
      });
      utterance.addEventListener('error', function () {
        var errorEvent = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
        status("speak failed: ".concat(errorEvent.message));
        patches.paused = false;
        patches.speaking = false;
        clearTimeout(timeoutResumeInfinity);
        reject(errorEvent);
      });

      // make sure we have no mem-leak
      clearTimeout(timeoutResumeInfinity);

      // do not cancel currently playing voice, if noStop option is true explicitly.
      if (!(noStop === true)) {
        internal.speechSynthesis.cancel();
      }
      setTimeout(function () {
        return internal.speechSynthesis.speak(utterance);
      }, 10);
    });
  };

  /** @private **/
  var debugUtterance = function debugUtterance(_ref5) {
    var voice = _ref5.voice,
      pitch = _ref5.pitch,
      rate = _ref5.rate,
      volume = _ref5.volume;
    var _ref6 = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {},
      _ref6$isMsNatural = _ref6.isMsNatural,
      isMsNatural = _ref6$isMsNatural === void 0 ? false : _ref6$isMsNatural;
    debug("utterance: voice=".concat(voice === null || voice === void 0 ? void 0 : voice.name, " volume=").concat(volume, " rate=").concat(rate, " pitch=").concat(pitch, " isMsNatural=").concat(isMsNatural));
  };

  /**
   * Timer variable to clear interval
   * @private
   */
  var timeoutResumeInfinity;

  /**
   * Fixes long texts in some browsers
   * @private
   * @param target
   */
  function resumeInfinity(target) {
    // prevent memory-leak in case utterance is deleted, while this is ongoing
    if (!target && timeoutResumeInfinity) {
      debug('force-clear timeout');
      return scope.clearTimeout(timeoutResumeInfinity);
    }

    // only execute on speaking utterances, otherwise paused
    // utterances will get resumed, thus breaking user experience
    // include internal patching, since some systems have problems with
    // pause/resume and updateing the internal state on speechSynthesis
    var _internal$speechSynth = internal.speechSynthesis,
      paused = _internal$speechSynth.paused,
      speaking = _internal$speechSynth.speaking;
    var isSpeaking = speaking || patches.speaking;
    var isPaused = paused || patches.paused;
    debug("resumeInfinity isSpeaking=".concat(isSpeaking, " isPaused=").concat(isPaused));
    if (isSpeaking && !isPaused) {
      internal.speechSynthesis.pause();
      internal.speechSynthesis.resume();
    }
    timeoutResumeInfinity = scope.setTimeout(function () {
      resumeInfinity(target);
    }, 5000);
  }

  /**
   * Cancels the current speaking, if any running
   */
  EasySpeech.cancel = function () {
    ensureInit();
    status('cancelling');
    internal.speechSynthesis.cancel();
    patches.paused = false;
    patches.speaking = false;
  };

  /**
   * Resumes to speak, if any paused
   */
  EasySpeech.resume = function () {
    ensureInit();
    status('resuming');
    patches.paused = false;
    patches.speaking = true;
    internal.speechSynthesis.resume();
  };

  /**
   * Pauses the current speaking, if any running
   */
  EasySpeech.pause = function () {
    ensureInit();
    status('pausing');

    // exec pause on Android causes speech to end but not to fire end-event
    // se we simply do it manually instead of pausing
    if (patches.isAndroid) {
      debug('patch pause on Android with cancel');
      return internal.speechSynthesis.cancel();
    }
    internal.speechSynthesis.pause();
    // in some cases, pause does not update the internal state,
    // so we need to update it manually using an own state
    patches.paused = true;
    patches.speaking = false;
  };

  /**
   * Resets the internal state to a default-uninitialized state
   */
  EasySpeech.reset = function () {
    Object.assign(internal, {
      status: 'reset',
      initialized: false,
      speechSynthesis: null,
      speechSynthesisUtterance: null,
      speechSynthesisVoice: null,
      speechSynthesisEvent: null,
      speechSynthesisErrorEvent: null,
      voices: null,
      defaultVoice: null,
      defaults: {
        pitch: 1,
        rate: 1,
        volume: 1,
        voice: null
      },
      handlers: {}
    });
  };

  return EasySpeech;

})();

;
/* academy-listen.js — "Listen to this module" for Renal Care Academy pages (Nov 26 2026, Dr. Rivero).
 *
 * Reads a module aloud with the device's own voice (Web Speech API, through the vendored easy-speech wrapper,
 * which the build concatenates in front of this file). Free, no server, no audio files, works offline in Schola.
 * Built for learners who cannot or should not look at the screen: people with low vision and people driving.
 *   - one tap plays the whole module straight through (title, every section, figure descriptions, tables);
 *     the quiz and the "read next" links are not read
 *   - big, high-contrast controls: back a section, play/pause, forward a section, speed, voice, close
 *   - the paragraph being read is highlighted and kept in view (unless the reader is scrolling)
 *   - the screen is kept awake while playing (Screen Wake Lock), so playback does not stop when it would dim
 *   - the place is remembered per module (localStorage rcm-tts:<path>); speed and voice are remembered too
 *   - pause is implemented as stop-and-remember, because pause() is unreliable on Android
 * Source file: edit this, then run tools/academy/apply_listen.py (writes assets/academy-listen.<hash>.js).
 */
(function () {
  "use strict";
  var ES = window.EasySpeech;
  if (!ES || !("speechSynthesis" in window) || !document.querySelector("main")) return;

  var PATH = location.pathname.replace(/\.html$/, "");
  var K_POS = "rcm-tts:" + PATH, K_RATE = "rcm-tts-rate", K_VOICE = "rcm-tts-voice";
  var RATES = [0.8, 1, 1.15, 1.3, 1.5, 1.75, 2];
  var SKIP_SECTIONS = { quiz: 1, reading: 1 };
  var reduceMotion = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---------- text: what to read ---------- */
  var BLOCK = "h1,h2,h3,h4,p,li,figcaption,tr,dt,dd,blockquote", LEAF = "p,li,figcaption,tr,dt,dd,blockquote";
  var UNIT = [
    [/(\d)\s?mL\/min\b/g, "$1 milliliters per minute"], [/(\d)\s?mL\/h\b/g, "$1 milliliters per hour"],
    [/(\d)\s?mL\b/g, "$1 milliliters"], [/(\d)\s?mg\/dL\b/g, "$1 milligrams per deciliter"],
    [/(\d)\s?mmol\/L\b/g, "$1 millimoles per liter"], [/(\d)\s?mEq\/L\b/g, "$1 milliequivalents per liter"],
    [/(\d)\s?g\/dL\b/g, "$1 grams per deciliter"], [/(\d)\s?g\/L\b/g, "$1 grams per liter"],
    [/(\d)\s?mg\b/g, "$1 milligrams"], [/(\d)\s?kg\b/g, "$1 kilograms"], [/(\d)\s?mmHg\b/g, "$1 millimeters of mercury"],
    [/(\d)\s?°C\b/g, "$1 degrees Celsius"], [/(\d)\s?%/g, "$1 percent"]
  ];
  function speakable(s) {
    s = s.replace(/\[\d+(?:[,–-]\s*\d+)*\]/g, "")                // citation markers [3] [2,4]
      .replace(/(\d)\s*[–—-]\s*(\d)/g, "$1 to $2")               // 4–6 -> 4 to 6
      .replace(/\be\.g\.,?/gi, "for example,").replace(/\bi\.e\.,?/gi, "that is,").replace(/\bvs\.?(?=\s)/gi, "versus")
      .replace(/≥/g, " greater than or equal to ").replace(/≤/g, " less than or equal to ")
      .replace(/\s>\s/g, " greater than ").replace(/\s<\s/g, " less than ")
      .replace(/→|⇒/g, " to ").replace(/×/g, " times ").replace(/±/g, " plus or minus ")
      .replace(/[µμ]g\b/g, " micrograms").replace(/·|•|&middot;/g, ", ").replace(/[“”]/g, '"').replace(/[‘’]/g, "'");
    UNIT.forEach(function (u) { s = s.replace(u[0], u[1]); });
    return s.replace(/\s+([,.;:!?])/g, "$1").replace(/\s+/g, " ").trim();
  }
  function visible(el) { return el.getClientRects().length > 0 && !el.closest(".lang-hidden,[hidden],[aria-hidden='true']"); }
  var EXCL = "button,svg,sup,script,style,.nc-cite,.rcn-bm,.rcm-tts-ui,[aria-hidden='true'],.lang-hidden,input,select,textarea";
  function cleanText(el) {
    var c = el.cloneNode(true);
    c.querySelectorAll(EXCL).forEach(function (n) { n.remove(); });
    return (c.textContent || "").replace(/\s+/g, " ").trim();
  }
  // Live text of an element with a map from each character back to its DOM text node, so a spoken sentence or
  // word can be highlighted in place (CSS Custom Highlight API: no change to the page's markup).
  function textMap(el) {
    var str = "", map = [], space = true;
    var w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: function (n) {
      var p = n.parentElement; return p && p !== el && p.closest(EXCL) && el.contains(p.closest(EXCL)) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT; } });
    for (var n = w.nextNode(); n; n = w.nextNode()) {
      var t = n.nodeValue;
      for (var i = 0; i < t.length; i++) {
        if (/\s/.test(t[i])) { if (!space) { str += " "; map.push([n, i]); space = true; } }
        else { str += t[i]; map.push([n, i]); space = false; }
      }
    }
    if (str.endsWith(" ")) { str = str.slice(0, -1); map.pop(); }
    return { str: str, map: map };
  }
  function rangeOf(m, a, b) {
    if (!m || a < 0 || b <= a || b > m.map.length) return null;
    var r = document.createRange(), s0 = m.map[a], s1 = m.map[b - 1];
    try { r.setStart(s0[0], s0[1]); r.setEnd(s1[0], s1[1] + 1); } catch (e) { return null; }
    return r;
  }
  function tableRowText(tr) {
    var table = tr.closest("table"), cells = Array.prototype.slice.call(tr.children);
    if (!cells.length || tr.closest("thead") || cells.every(function (c) { return c.tagName === "TH"; }) && tr === table.rows[0]) return "";
    var head = table.tHead && table.tHead.rows[0] || (table.rows[0] && Array.prototype.every.call(table.rows[0].cells, function (c) { return c.tagName === "TH"; }) ? table.rows[0] : null);
    var hs = head ? Array.prototype.map.call(head.cells, cleanText) : [];
    return cells.map(function (c, i) { var t = cleanText(c); return t ? (hs[i] && i > 0 ? hs[i] + ": " : "") + t : ""; })
      .filter(Boolean).join(". ");
  }
  function chunks(text) {                                         // sentences, at most ~220 characters each
    var out = [], parts = text.split(/(?<=[.!?:;])\s+(?=["(]?[A-Z0-9])/);
    parts.forEach(function (p) {
      while (p.length > 240) {
        var cut = p.lastIndexOf(", ", 220); if (cut < 80) cut = p.lastIndexOf(" ", 220); if (cut < 40) cut = 220;
        out.push(p.slice(0, cut + 1)); p = p.slice(cut + 1).trim();
      }
      if (p) out.push(p);
    });
    return out;
  }

  var items = [], sections = [];                                  // items: {el, sec, parts[]}
  function build() {
    items = []; sections = [];
    var h1 = document.querySelector(".hero h1, h1");
    if (h1) items.push({ el: h1, sec: -1, parts: chunks(speakable(cleanText(h1))) });
    var main = document.querySelector("main");
    main.querySelectorAll("section.section").forEach(function (sec) {
      if (SKIP_SECTIONS[sec.id] || !visible(sec)) {
        if (sec.id === "quiz") items.push({ el: sec.querySelector("h2") || sec, sec: sections.length - 1, note: 1,
          parts: ["This module ends with a short quiz. Open it on screen when it is safe to do so. End of module."] });
        return;
      }
      var h2 = sec.querySelector("h2");
      sections.push({ el: sec, title: h2 ? cleanText(h2) : "", first: items.length });
      var si = sections.length - 1;
      sec.querySelectorAll(BLOCK).forEach(function (el) {
        if (!visible(el) || el.closest("form,fieldset,.nc-nextprev,.calc-cards-wrap,.section-tag,.nc-cite,.rcm-tts-ui")) return;
        var tag = el.tagName, text;
        if (tag === "TR") text = tableRowText(el);
        else if (tag === "FIGCAPTION") { var d = el.querySelector(".fig-desc"); text = d ? cleanText(d) : cleanText(el); if (text) text = "Figure. " + text; }
        else {
          if (el.closest("figcaption,tr") || el.querySelector(LEAF)) return; // read leaves only
          text = cleanText(el);
        }
        if (tag === "TR" || tag === "FIGCAPTION") {                 // composite text: paragraph highlight only
          text = speakable(text || "");
          if (text.length > 1) items.push({ el: el, sec: si, parts: chunks(text) });
          return;
        }
        var m = textMap(el);
        if (m.str !== text) m = null;                               // map must match what is read, else no in-text highlight
        var raw = chunks(text), parts = [], spans = [], at = 0;
        raw.forEach(function (r) {
          var a = m ? m.str.indexOf(r, at) : -1;
          if (a >= 0) at = a + r.length;
          var say = speakable(r);
          if (say.length > 1) { parts.push(say); spans.push(a >= 0 ? { a: a, b: a + r.length, same: say === r.trim() } : null); }
        });
        if (parts.length) items.push({ el: el, sec: si, parts: parts, spans: spans, map: m });
      });
    });
    if (!items.some(function (it) { return it.note; })) items.push({ el: null, sec: sections.length - 1, note: 1, parts: ["End of module."] });
  }

  /* ---------- player state ---------- */
  var idx = 0, part = 0, playing = false, token = 0, voice = null, rate = parseFloat(ls(K_RATE)) || 1, ready = null, wake = null;
  var lastUserScroll = 0, ui = null, statusEl, secEl, playBtn, rateBtn, voiceSel;
  ["wheel", "touchmove", "keydown"].forEach(function (ev) { window.addEventListener(ev, function (e) { if (ev !== "keydown" || /Arrow|Page|Home|End|Space/.test(e.code || "")) lastUserScroll = Date.now(); }, { passive: true }); });

  // Apple puts the voice quality in the voiceURI (com.apple.voice.premium.en-US.Ava); names are often just "Ava".
  function tier(v) {
    var k = (v.voiceURI || "") + " " + v.name;
    return /premium/i.test(k) ? "Premium" : /enhanced/i.test(k) ? "Enhanced" : "";
  }
  var REGION = { US: "US", GB: "UK", AU: "Australia", IN: "India", IE: "Ireland", ZA: "South Africa", PH: "Philippines",
    NZ: "New Zealand", SG: "Singapore", CA: "Canada", "GB-SCT": "Scotland" };
  function voiceLabel(v) {
    var name = v.name.replace(/\s*\((?:premium|enhanced|compact)\)\s*/ig, " ").replace(/\s+/g, " ").trim();
    var m = /^en[-_]([A-Za-z-]+)/.exec(v.lang || ""), reg = m ? (REGION[m[1].toUpperCase()] || m[1].toUpperCase()) : "";
    var t = tier(v);
    return name + (t ? " \u00b7 " + t : "") + (reg && name.indexOf(reg) < 0 ? " (" + reg + ")" : "");
  }
  function init() {
    if (!ready) ready = ES.init({ maxTimeout: 5000, interval: 250, quiet: true }).catch(function () { return false; }).then(function () {
      var vs = (ES.voices() || []).filter(function (v) { return /^en([-_]|$)/i.test(v.lang); });
      var score = function (v) { var t = tier(v); return (t === "Premium" ? 8 : t === "Enhanced" ? 6 : /natural|neural|siri|google/i.test(v.name) ? 4 : 0) + (/en[-_](US|PH)/i.test(v.lang) ? 2 : 0) + (v.localService ? 1 : 0); };
      vs.sort(function (a, b) { return score(b) - score(a) || a.name.localeCompare(b.name); });
      var saved = ls(K_VOICE);
      voice = vs.filter(function (v) { return v.voiceURI === saved || v.name === saved; })[0] || vs[0] || null;
      return vs;
    });
    return ready;
  }

  function mark() {
    document.querySelectorAll(".rcm-tts-cur").forEach(function (n) { n.classList.remove("rcm-tts-cur"); });
    var it = items[idx]; if (!it || !it.el) return;
    it.el.classList.add("rcm-tts-cur");
    if (Date.now() - lastUserScroll > 6000) {
      var r = it.el.getBoundingClientRect(), vh = innerHeight;
      if (r.top < 70 || r.bottom > vh - 130) it.el.scrollIntoView({ block: "center", behavior: reduceMotion ? "auto" : "smooth" });
    }
    var s = sections[it.sec];
    if (secEl) secEl.textContent = it.sec < 0 ? "Introduction" : (s ? "Section " + (it.sec + 1) + " of " + sections.length + ": " + s.title : "");
  }
  var HL = window.CSS && CSS.highlights && window.Highlight ? CSS.highlights : null;
  function hl(name, range) { if (!HL) return; if (range) HL.set(name, new Highlight(range)); else HL.delete(name); }
  function hlSentence() {
    var it = items[idx], sp = it && it.spans && it.spans[part];
    hl("rcm-tts-word", null);
    hl("rcm-tts-sent", sp ? rangeOf(it.map, sp.a, sp.b) : null);
  }
  function hlWord(ci) {
    var it = items[idx], sp = it && it.spans && it.spans[part];
    if (!sp || !sp.same || typeof ci !== "number") return;
    var str = it.map.str, a = sp.a + ci;
    while (a < sp.b && /\s/.test(str[a])) a++;
    var b = a; while (b < sp.b && !/\s/.test(str[b])) b++;
    while (b > a && /[,.;:!?)"']/.test(str[b - 1])) b--;
    hl("rcm-tts-word", rangeOf(it.map, a, b));
  }
  function save() { ls(K_POS, JSON.stringify({ i: idx, t: Date.now() })); }

  function speakNext() {
    var my = ++token;
    if (!playing) return;
    var it = items[idx];
    if (!it) { finish(); return; }
    if (part >= it.parts.length) { idx++; part = 0; save(); speakNext(); return; }
    if (part === 0) mark();
    hlSentence();
    ES.speak({ text: it.parts[part], voice: voice || undefined, rate: rate, pitch: 1, volume: 1, force: true,
      boundary: function (e) { if (my === token && e && (e.name === "word" || !e.name)) hlWord(e.charIndex); },
      end: function () { if (my !== token) return; part++; speakNext(); },
      error: function (e) { if (my !== token) return; if (e && /interrupted|canceled/.test(e.error || "")) return; part++; speakNext(); }
    }).catch(function () {});
  }
  function play() {
    init().then(function () {
      if (!items.length) build();
      playing = true; setUI(); keepAwake(true); speakNext();
    });
  }
  function stop(keep) { hl("rcm-tts-word", null); playing = false; token++; try { ES.cancel(); } catch (e) {} keepAwake(false); setUI(); if (keep) save(); }
  function finish() { stop(false); idx = 0; part = 0; ls(K_POS, null); mark(); status("Finished. Tap play to listen again."); }
  function jumpSection(d) {
    var cur = items[idx] ? items[idx].sec : -1, target = Math.max(-1, Math.min(sections.length - 1, cur + d));
    if (d < 0 && items[idx] && sections[cur] && idx > sections[cur].first + 1) target = cur;   // back = start of this section first
    idx = target < 0 ? 0 : sections[target].first; part = 0; save();
    if (playing) { token++; try { ES.cancel(); } catch (e) {} setTimeout(speakNext, 60); } else mark();
  }
  function keepAwake(on) {
    if (!("wakeLock" in navigator)) return;
    if (on && !wake) navigator.wakeLock.request("screen").then(function (w) { wake = w; w.addEventListener("release", function () { wake = null; }); }).catch(function () {});
    if (!on && wake) { wake.release().catch(function () {}); wake = null; }
  }
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "visible" && playing) keepAwake(true);
  });
  window.addEventListener("pagehide", function () { if (playing) stop(true); });

  /* ---------- UI ---------- */
  var IC = {
    play: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>',
    pause: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z" fill="currentColor"/></svg>',
    prev: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h2v14H6zM19 5.5v13L9 12z" fill="currentColor"/></svg>',
    next: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 5h2v14h-2zM5 5.5v13L15 12z" fill="currentColor"/></svg>',
    close: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>',
    head: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 14v-2a8 8 0 0 1 16 0v2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><rect x="3" y="13" width="4.5" height="7" rx="1.6" fill="currentColor"/><rect x="16.5" y="13" width="4.5" height="7" rx="1.6" fill="currentColor"/></svg>'
  };
  function status(t) { if (statusEl) statusEl.textContent = t; }
  function setUI() {
    if (!playBtn) return;
    playBtn.innerHTML = playing ? IC.pause : IC.play;
    playBtn.setAttribute("aria-label", playing ? "Pause" : "Play");
    playBtn.setAttribute("aria-pressed", playing ? "true" : "false");
    status(playing ? "Reading aloud" : "Paused");
    document.body.classList.toggle("rcm-tts-playing", playing);
  }
  function rateLabel() { return (rate === 1 ? "1" : String(rate)) + "×"; }

  function openPlayer() {
    if (!ui) {
      ui = document.createElement("div");
      ui.className = "rcm-tts-ui rcm-tts-bar no-print";
      ui.setAttribute("role", "region");
      ui.setAttribute("aria-label", "Listen to this module");
      ui.innerHTML =
        '<div class="rcm-tts-info"><span class="rcm-tts-status" aria-live="polite">Paused</span><span class="rcm-tts-sec"></span></div>' +
        '<div class="rcm-tts-ctrls">' +
          '<button type="button" class="rcm-tts-b" data-a="prev" aria-label="Previous section">' + IC.prev + '</button>' +
          '<button type="button" class="rcm-tts-b rcm-tts-play" data-a="play" aria-label="Play" aria-pressed="false">' + IC.play + '</button>' +
          '<button type="button" class="rcm-tts-b" data-a="next" aria-label="Next section">' + IC.next + '</button>' +
          '<button type="button" class="rcm-tts-b rcm-tts-rate" data-a="rate" aria-label="Reading speed">' + rateLabel() + '</button>' +
          '<label class="rcm-tts-vl"><span class="rcm-tts-sr">Voice</span><select class="rcm-tts-voice" aria-label="Voice"></select></label>' +
          '<button type="button" class="rcm-tts-b rcm-tts-x" data-a="close" aria-label="Stop and close the player">' + IC.close + '</button>' +
        '</div>';
      document.body.appendChild(ui);
      statusEl = ui.querySelector(".rcm-tts-status"); secEl = ui.querySelector(".rcm-tts-sec");
      playBtn = ui.querySelector(".rcm-tts-play"); rateBtn = ui.querySelector(".rcm-tts-rate"); voiceSel = ui.querySelector(".rcm-tts-voice");
      ui.addEventListener("click", function (e) {
        var b = e.target.closest("button[data-a]"); if (!b) return;
        var a = b.getAttribute("data-a");
        if (a === "play") { if (playing) stop(true); else play(); }
        else if (a === "prev") jumpSection(-1);
        else if (a === "next") jumpSection(1);
        else if (a === "rate") {
          rate = RATES[(RATES.indexOf(rate) + 1) % RATES.length] || 1; ls(K_RATE, String(rate)); rateBtn.textContent = rateLabel();
          rateBtn.setAttribute("aria-label", "Reading speed " + rateLabel());
          if (playing) { token++; try { ES.cancel(); } catch (x) {} setTimeout(speakNext, 60); }
        } else if (a === "close") closePlayer();
      });
      voiceSel.addEventListener("change", function () {
        var vs = ES.voices() || []; voice = vs.filter(function (v) { return v.voiceURI === voiceSel.value; })[0] || voice;
        if (voice) ls(K_VOICE, voice.voiceURI);
        if (playing) { token++; try { ES.cancel(); } catch (x) {} setTimeout(speakNext, 60); }
      });
      init().then(function (vs) {
        (vs || []).forEach(function (v) {
          var o = document.createElement("option"); o.value = v.voiceURI;
          o.textContent = voiceLabel(v);
          if (voice && v.voiceURI === voice.voiceURI) o.selected = true;
          voiceSel.appendChild(o);
        });
        if (!vs || !vs.length) { status("This device has no English voice installed."); voiceSel.disabled = true; }
      });
    }
    ui.hidden = false;
    document.body.classList.add("rcm-tts-on");
    build();
    playBtn.focus({ preventScroll: true });
  }
  function closePlayer() {
    stop(true);
    document.querySelectorAll(".rcm-tts-cur").forEach(function (n) { n.classList.remove("rcm-tts-cur"); });
    hl("rcm-tts-sent", null); hl("rcm-tts-word", null);
    if (ui) ui.hidden = true;
    document.body.classList.remove("rcm-tts-on");
    if (launch) launch.focus({ preventScroll: true });
  }

  /* ---------- launch button (in the hero, under the title) ---------- */
  var launch = null;
  function addLaunch() {
    var anchor = document.querySelector(".hero .hero-meta") || document.querySelector(".hero h1");
    if (!anchor) return;
    var saved = null; try { saved = JSON.parse(ls(K_POS) || "null"); } catch (e) {}
    launch = document.createElement("button");
    launch.type = "button";
    launch.className = "rcm-tts-ui rcm-tts-launch no-print";
    launch.innerHTML = IC.head + '<span>' + (saved && saved.i > 0 ? "Resume listening" : "Listen to this module") + '</span>';
    launch.setAttribute("aria-label", (saved && saved.i > 0 ? "Resume listening to" : "Listen to") + " this module, read aloud by your device");
    launch.addEventListener("click", function () {
      openPlayer();
      if (saved && saved.i > 0 && saved.i < items.length) { idx = saved.i; part = 0; } else { idx = 0; part = 0; }
      saved = null;
      play();
    });
    anchor.parentNode.insertBefore(launch, anchor.nextSibling);
  }

  var css = document.createElement("style");
  css.id = "rcm-tts-css";
  css.textContent = [
    ".rcm-tts-launch{display:inline-flex;align-items:center;gap:9px;margin:14px 0 4px;padding:12px 20px 12px 16px;min-height:48px;border-radius:999px;border:2px solid #1F3864;background:#1F3864;color:#fff;font:700 16px/1.1 Inter,Manrope,system-ui,sans-serif;cursor:pointer;box-shadow:0 6px 16px -8px rgba(20,40,75,.55)}",
    ".rcm-tts-launch svg{width:22px;height:22px}.rcm-tts-launch:hover{background:#16294a}",
    ".rcm-tts-launch:focus-visible,.rcm-tts-b:focus-visible,.rcm-tts-voice:focus-visible{outline:3px solid #f0a81e;outline-offset:2px}",
    ".rcm-tts-bar{position:fixed;z-index:100002;left:50%;bottom:16px;transform:translateX(-50%);width:min(640px,calc(100% - 150px));background:#13233f;color:#fff;border-radius:18px;padding:10px 12px;box-shadow:0 14px 40px -10px rgba(0,0,0,.55);border:1px solid rgba(255,255,255,.14);font-family:Inter,Manrope,system-ui,sans-serif}",
    ".rcm-tts-bar[hidden]{display:none}",
    ".rcm-tts-info{display:flex;gap:10px;align-items:baseline;min-width:0;padding:0 4px 8px}",
    ".rcm-tts-status{font:800 12px/1 Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#f3c46a;flex:none}",
    ".rcm-tts-sec{font-size:14px;color:#e6edf8;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}",
    ".rcm-tts-ctrls{display:flex;align-items:center;gap:8px}",
    ".rcm-tts-b{flex:none;display:inline-flex;align-items:center;justify-content:center;width:52px;height:52px;border-radius:14px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.08);color:#fff;cursor:pointer;font:800 16px/1 Inter,sans-serif}",
    ".rcm-tts-b svg{width:26px;height:26px}.rcm-tts-b:hover{background:rgba(255,255,255,.16)}",
    ".rcm-tts-play{width:64px;height:64px;border-radius:50%;background:#f0a81e;border-color:#f0a81e;color:#13233f}.rcm-tts-play:hover{background:#ffc04a}",
    ".rcm-tts-play svg{width:32px;height:32px}",
    ".rcm-tts-x{margin-left:auto}",
    ".rcm-tts-vl{flex:1;min-width:0}.rcm-tts-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}",
    ".rcm-tts-voice{width:100%;min-width:0;height:52px;border-radius:14px;border:1px solid rgba(255,255,255,.22);background:#1d3157;color:#fff;font:600 15px Inter,sans-serif;padding:0 10px}",
    ".rcm-tts-cur{background:#fff8dc !important;box-shadow:0 0 0 6px #fff8dc;border-radius:4px;color:#1e2a38 !important}",
    "::highlight(rcm-tts-sent){background-color:#ffe38f;color:#1e2a38}",
    "::highlight(rcm-tts-word){background-color:#f0a81e;color:#111}",
    "html[data-theme='dark'] .rcm-tts-cur{background:#2b2717 !important;box-shadow:0 0 0 6px #2b2717;color:#fff6dc !important}",
    "html[data-theme='dark'] ::highlight(rcm-tts-sent){background-color:#6b5414;color:#fff}",
    "html[data-theme='dark'] ::highlight(rcm-tts-word){background-color:#f0a81e;color:#111}",
    "html[data-theme='dark'] .rcm-tts-launch{background:#f0a81e;border-color:#f0a81e;color:#13233f}",
    "body.rcm-tts-on{padding-bottom:140px}",
    "body.rcm-tts-on .rcn-toast,body.rcm-tts-on .rcn-resume{display:none !important}",
    "@media (max-width:640px){.rcm-tts-bar{width:calc(100% - 16px);bottom:8px;padding:10px}",
    "  .rcm-tts-ctrls{flex-wrap:wrap;gap:8px}.rcm-tts-b{width:50px;height:50px}.rcm-tts-play{width:60px;height:60px}",
    "  .rcm-tts-vl{order:9;flex:1 1 100%}.rcm-tts-voice{height:42px;font-size:14px}",
    "  body.rcm-tts-on{padding-bottom:200px}",
    "  body.rcm-tts-on .float-controls,body.rcm-tts-on .float-controls-left,body.rcm-tts-on .scroll-top-btn,body.rcm-tts-on .rcn-fab,body.rcm-tts-on .print-btn{translate:0 -178px !important}}",
    "@media print{.rcm-tts-ui{display:none !important}.rcm-tts-cur{background:none !important;box-shadow:none !important}}"
  ].join("\n");
  document.head.appendChild(css);

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", addLaunch); else addLaunch();
})();
