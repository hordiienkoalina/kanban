const cards = document.querySelectorAll('.card')
const dropzones = document.querySelectorAll('.dropzone')

cards.forEach(card => {
card.addEventListener('dragstart', dragstart)
card.addEventListener('dragend', dragend)
})

function dragstart() {
dropzones.forEach(dropzone => dropzone.classList.add('highlight'))

this.classList.add('is-dragging')
}

function dragend() {
dropzones.forEach(dropzone => dropzone.classList.remove('highlight'))

this.classList.remove('is-dragging')
}

dropzones.forEach(dropzone => {
dropzone.addEventListener('dragover', dragover)
dropzone.addEventListener('dragleave', dragleave)
dropzone.addEventListener('drop', drop)
})


function dragover() {
this.classList.add('over')

const cardBeingDragged = document.querySelector('.is-dragging')

this.appendChild(cardBeingDragged)
}

function dragleave() {
this.classList.remove('over')
}

function drop() {
this.classList.remove('over')
}

const modal = document.querySelector(".modal");
const trigger = document.querySelector(".trigger");
const closeButton = document.querySelector(".close-button");

function toggleModal() {
    modal.classList.toggle("show-modal");
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

trigger.addEventListener("click", toggleModal);
closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);
