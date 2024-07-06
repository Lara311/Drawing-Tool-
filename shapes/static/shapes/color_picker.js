document.addEventListener('DOMContentLoaded', (event) => {
    const colorInput = document.getElementById('color');
    const colorPreview = document.getElementById('color-preview');

    if (colorInput && colorPreview) {
        colorInput.addEventListener('input', (event) => {
            const color = event.target.value;
            colorPreview.style.backgroundColor = color;
        });
    }
});
