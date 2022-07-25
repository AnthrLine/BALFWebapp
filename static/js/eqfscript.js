const LIST1 = document.getElementById(1)
const TABLE1 = document.getElementById("t1")
let state1 = true

const LIST2 = document.getElementById(2)
const TABLE2 = document.getElementById("t2")
let state2 = true

const LIST3 = document.getElementById(3)
const TABLE3 = document.getElementById("t3")
let state3 = true

const LIST4 = document.getElementById(4)
const TABLE4= document.getElementById("t4")
let state4 = true

const LIST5 = document.getElementById(5)
const TABLE5= document.getElementById("t5")
let state5 = true

const LIST6 = document.getElementById(6)
const TABLE6 = document.getElementById("t6")
let state6 = true

const LIST7 = document.getElementById(7)
const TABLE7= document.getElementById("t7")
let state7 = true

window.addEventListener('load', function () {

	LIST1.onclick = function () {
	if (state1 === false) {
		TABLE1.classList.add('hidden');
		state1 = true
	}else{
		TABLE1.classList.remove('hidden');
		state1 = false
	}
}

LIST2.onclick = function () {
	if (state2 === false) {
		TABLE2.classList.add('hidden');
		state2 = true
	}else{
		TABLE2.classList.remove('hidden');
		state2 = false
	}
}

LIST3.onclick = function () {
	if (state3 === false) {
		TABLE3.classList.add('hidden');
		state3 = true
	}else{
		TABLE3.classList.remove('hidden');
		state3 = false
	}
}

	LIST4.onclick = function () {
		if (state4 === false) {
			TABLE4.classList.add('hidden');
			state4 = true
		}else{
			TABLE4.classList.remove('hidden');
			state4 = false
		}
	}

	LIST5.onclick = function () {
		if (state5 === false) {
			TABLE5.classList.add('hidden');
			state5 = true
		}else{
			TABLE5.classList.remove('hidden');
			state5 = false
		}
	}

	LIST6.onclick = function () {
		if (state6 === false) {
			TABLE6.classList.add('hidden');
			state6 = true
		}else{
			TABLE6.classList.remove('hidden');
			state6 = false
		}
	}

	LIST7.onclick = function () {
		if (state7 === false) {
			TABLE7.classList.add('hidden');
			state7 = true
		}else{
			TABLE7.classList.remove('hidden');
			state7 = false
		}
	}
})