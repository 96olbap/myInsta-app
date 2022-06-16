const likeBtn = document.querySelector('.like-btn');
let likeIcon = document.querySelector('#icon');
let count = document.querySelector('#count');

const bmBtn = document.querySelector('.bkmark-btn');
let bmIcon = document.querySelector('#bookmark');


// Btn clicked
let clicked = false;

likeBtn.addEventListener('click', () => {
    if (!clicked) {
        clicked = true;
        likeIcon.innerHTML = `<i class="fa-solid fa-heart"></i>`
        count.textContent++;
    } else {
        clicked = false;
        likeIcon.innerHTML = `<i class="fa-regular fa-heart"></i>`
        count.textContent--;
    }

    console.log('hello');
})

bmBtn.addEventListener('click', () => {
    if (!clicked) {
        clicked = true;
        bmIcon.innerHTML = `<i class="fa-solid fa-bookmark"></i>`
    } else {
        clicked = false;
        bmIcon.innerHTML = `<i class="fa-regular fa-bookmark"></i>`
    }

    console.log('hello');
})