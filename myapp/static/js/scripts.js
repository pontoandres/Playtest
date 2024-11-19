document.addEventListener('DOMContentLoaded', function() {
    // Dropdown functionality
    const dropdown = document.querySelector('.dropdown');
    const dropbtn = document.querySelector('.dropbtn');
    const dropdownContent = document.querySelector('.dropdown-content');

    if (dropbtn) {
        dropbtn.addEventListener('click', function(event) {
            event.stopPropagation();
            dropdownContent.classList.toggle('show');
        });

        document.addEventListener('click', function(event) {
            if (!dropdown.contains(event.target)) {
                dropdownContent.classList.remove('show');
            }
        });
    }

    // Comment form functionality
    const commentForm = document.getElementById('comment-form');
    if (commentForm) {
        commentForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const form = event.target;
            const formData = new FormData(form);
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '', true);
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    if (response.success) {
                        const commentList = document.getElementById('comments-list');
                        const newComment = document.createElement('li');
                        newComment.innerHTML = `<p>${response.text}</p><p><small>Por ${response.author} el ${response.created_at}</small></p>`;
                        commentList.appendChild(newComment);
                        form.reset();
                    } else {
                        alert('Error: ' + JSON.stringify(response.errors));
                    }
                }
            };
            xhr.send(formData);
        });
    }


    // Nueva funcionalidad: Mostrar detalles del juego en la columna derecha
    const gameLinks = document.querySelectorAll('.game-link');
    const gameDetails = document.getElementById('game-details');

    gameLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();

            // Obtener el ID del juego desde el atributo data-game-id
            const gameId = this.getAttribute('data-game-id');

            // Llamada AJAX para obtener los detalles del juego
            fetch(`/game/${gameId}/details/`)
                .then(response => response.json())
                .then(data => {
                    // Actualizar la sección de detalles con la información del juego
                    gameDetails.innerHTML = `
                        <img src="${data.image}" alt="${data.title}" class="img-fluid" style="border-radius: 8px; margin-bottom: 10px;">
                        <h2>${data.title}</h2>
                        <p>${data.description}</p>
                        <a href="/game/${gameId}/" class="btn btn-primary mt-3">Ver Perfil Completo</a>
                    `;
                })
                .catch(error => {
                    console.error('Error al cargar los detalles del juego:', error);
                    gameDetails.innerHTML = `<p>Hubo un error al cargar los detalles. Intenta de nuevo más tarde.</p>`;
                });
        });
    });
});
