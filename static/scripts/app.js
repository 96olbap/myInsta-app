const likeBtn = document.querySelector('.like-btn');
let likeIcon = document.querySelector('#icon');
let count = document.querySelector('#count');


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