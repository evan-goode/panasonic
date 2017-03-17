"use strict";

document.querySelector(".color").textContent = cheapest.color;
document.querySelector(".color").classList.add(cheapest.color);
document.querySelector(".price").textContent = cheapest.price;
var _iteratorNormalCompletion = true;
var _didIteratorError = false;
var _iteratorError = undefined;

try {
	for (var _iterator = document.querySelectorAll(".link")[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
		var element = _step.value;

		element.href = cheapest.link;
	}
} catch (err) {
	_didIteratorError = true;
	_iteratorError = err;
} finally {
	try {
		if (!_iteratorNormalCompletion && _iterator.return) {
			_iterator.return();
		}
	} finally {
		if (_didIteratorError) {
			throw _iteratorError;
		}
	}
}