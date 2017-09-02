"use strict";

var load = function () {
	var _ref = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee() {
		var response, cheapest, _iteratorNormalCompletion, _didIteratorError, _iteratorError, _iterator, _step, element;

		return regeneratorRuntime.wrap(function _callee$(_context) {
			while (1) {
				switch (_context.prev = _context.next) {
					case 0:
						_context.next = 2;
						return fetch("cheapest.json");

					case 2:
						response = _context.sent;
						_context.next = 5;
						return response.json();

					case 5:
						cheapest = _context.sent;

						console.log(cheapest);
						document.querySelector(".color").textContent = cheapest.color;
						document.querySelector(".color").classList.add(cheapest.color);
						document.querySelector(".price").textContent = cheapest.price_text;
						_iteratorNormalCompletion = true;
						_didIteratorError = false;
						_iteratorError = undefined;
						_context.prev = 13;
						for (_iterator = document.querySelectorAll(".link")[Symbol.iterator](); !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
							element = _step.value;

							element.href = cheapest.link;
						}
						_context.next = 21;
						break;

					case 17:
						_context.prev = 17;
						_context.t0 = _context["catch"](13);
						_didIteratorError = true;
						_iteratorError = _context.t0;

					case 21:
						_context.prev = 21;
						_context.prev = 22;

						if (!_iteratorNormalCompletion && _iterator.return) {
							_iterator.return();
						}

					case 24:
						_context.prev = 24;

						if (!_didIteratorError) {
							_context.next = 27;
							break;
						}

						throw _iteratorError;

					case 27:
						return _context.finish(24);

					case 28:
						return _context.finish(21);

					case 29:
					case "end":
						return _context.stop();
				}
			}
		}, _callee, this, [[13, 17, 21, 29], [22,, 24, 28]]);
	}));

	return function load() {
		return _ref.apply(this, arguments);
	};
}();

function _asyncToGenerator(fn) { return function () { var gen = fn.apply(this, arguments); return new Promise(function (resolve, reject) { function step(key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { return Promise.resolve(value).then(function (value) { step("next", value); }, function (err) { step("throw", err); }); } } return step("next"); }); }; }

load();