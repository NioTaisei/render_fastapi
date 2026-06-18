document.addEventListener('DOMContentLoaded', function () {
    const countElement = document.querySelector('.count');
    const incrementButton = document.querySelector('#increment');
    const decrementButton = document.querySelector('#decrement');

    let count = 0;

    incrementButton.addEventListener('click', function () {
        count++;
        updateCount();
    });

    decrementButton.addEventListener('click', function () {
        if (count > 0) {
            count--;
            updateCount();
        }
    });

    function updateCount() {
        countElement.textContent = count;
    }
});