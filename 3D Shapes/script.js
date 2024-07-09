document.addEventListener('DOMContentLoaded', () => {
    const box = document.getElementById('box');
    const container = document.querySelector('.container');
    let isDragging = false;
    let startX, startY, currentX = 0, currentY = 0;
    let scale = 1;

    document.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.clientX - currentX;
        startY = e.clientY - currentY;
    });

    document.addEventListener('mousemove', (e) => {
        if(isDragging) {
            currentX = e.clientX - startX;
            currentY = e.clientY - startY;

            if(currentY < -180) {
                currentY = -180;
            } else if(currentY > 0) {
                currentY = 0;
            }

            box.style.transform = `rotateX(${currentY}deg) rotateY(${currentX}deg)`;
        }
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
    });

    document.addEventListener('mouseleave', () => {
        isDragging = false;
    });
    
    document.addEventListener('wheel', (e) => {
        if(e.deltaY > 0) {
            scale -= 0.1;
        } else if (e.deltaY < 0) {
            scale += 0.1;
        }
        scale = Math.min(Math.max(scale, 0.1), 3);
        container.style.transform = `translate(-50%, -50%) scale(${scale})`;
    });
});