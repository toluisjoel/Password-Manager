function play() {
    let viewCloseBtns = document.getElementsByClassName('more_less')
    for (button of viewCloseBtns) {
        button = button
        button.addEventListener('click', (e) => {
            e.preventDefault();
            button.innerHTMl = 'less'
            button.style.backgroundColor = '#0056';
        });
    }
}