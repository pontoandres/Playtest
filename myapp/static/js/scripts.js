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

    // Modal functionality
    // window.showGameDetails = function(gameId) {
    //     // AJAX logic to load game details into the modal
    //     fetch(`/game/${gameId}/`)
    //         .then(response => response.text())
    //         .then(data => {
    //             document.getElementById('modal-body').innerHTML = data;
    //             document.getElementById('gameModal').style.display = 'block';
    //         })
    //         .catch(error => console.error('Error loading game details:', error));
    // }

    // window.closeModal = function() {
    //     document.getElementById('gameModal').style.display = 'none';
    // }

    // Close the modal when clicking outside of it
    // window.onclick = function(event) {
    //     var modal = document.getElementById('gameModal');
    //     if (event.target == modal) {
    //         modal.style.display = 'none';
    //     }
    // }
});