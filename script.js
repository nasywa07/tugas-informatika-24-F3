// Data pilihan permainan
const choices = {
    batu: { emoji: '🪨', name: 'Batu' },
    kertas: { emoji: '📄', name: 'Kertas' },
    gunting: { emoji: '✂️', name: 'Gunting' }
};

// Skor permainan
let scores = {
    player: 0,
    computer: 0,
    draw: 0
};

// Logika pemenang
const winConditions = {
    batu: 'gunting',      // Batu mengalahkan Gunting
    kertas: 'batu',       // Kertas mengalahkan Batu
    gunting: 'kertas'     // Gunting mengalahkan Kertas
};

// Inisialisasi event listener untuk tombol pilihan
document.querySelectorAll('.choice-btn').forEach(button => {
    button.addEventListener('click', function() {
        const playerChoice = this.dataset.choice;
        playGame(playerChoice);
    });
});

// Fungsi utama permainan
function playGame(playerChoice) {
    // Hapus kelas active dari semua tombol
    document.querySelectorAll('.choice-btn').forEach(btn => {
        btn.classList.remove('active');
    });

    // Tambah kelas active ke tombol yang dipilih
    document.querySelector(`[data-choice="${playerChoice}"]`).classList.add('active');

    // Pilihan komputer secara acak
    const computerChoice = getComputerChoice();

    // Tampilkan pilihan player dan komputer
    displayChoices(playerChoice, computerChoice);

    // Tentukan pemenang dan update skor
    const result = determineWinner(playerChoice, computerChoice);
    updateScore(result);

    // Tampilkan hasil
    displayResult(result, playerChoice, computerChoice);
}

// Fungsi untuk mendapatkan pilihan komputer secara acak
function getComputerChoice() {
    const choiceArray = Object.keys(choices);
    const randomIndex = Math.floor(Math.random() * choiceArray.length);
    return choiceArray[randomIndex];
}

// Fungsi untuk menampilkan pilihan player dan komputer
function displayChoices(playerChoice, computerChoice) {
    const playerChoiceDiv = document.getElementById('playerChoice');
    const computerChoiceDiv = document.getElementById('computerChoice');

    playerChoiceDiv.innerHTML = `
        <div class="choice-emoji">${choices[playerChoice].emoji}</div>
        <div class="choice-name">${choices[playerChoice].name}</div>
    `;

    computerChoiceDiv.innerHTML = `
        <div class="choice-emoji">${choices[computerChoice].emoji}</div>
        <div class="choice-name">${choices[computerChoice].name}</div>
    `;
}

// Fungsi untuk menentukan pemenang
function determineWinner(playerChoice, computerChoice) {
    if (playerChoice === computerChoice) {
        return 'draw';
    }

    if (winConditions[playerChoice] === computerChoice) {
        return 'win';
    }

    return 'lose';
}

// Fungsi untuk update skor
function updateScore(result) {
    switch(result) {
        case 'win':
            scores.player++;
            break;
        case 'lose':
            scores.computer++;
            break;
        case 'draw':
            scores.draw++;
            break;
    }

    // Update display skor
    document.getElementById('playerScore').textContent = scores.player;
    document.getElementById('computerScore').textContent = scores.computer;
    document.getElementById('drawScore').textContent = scores.draw;
}

// Fungsi untuk menampilkan hasil
function displayResult(result, playerChoice, computerChoice) {
    const resultSection = document.getElementById('resultSection');
    const resultMessage = document.getElementById('resultMessage');
    const resultDetail = document.getElementById('resultDetail');

    // Reset kelas
    resultMessage.className = 'result-message';

    let message = '';
    let detail = '';

    switch(result) {
        case 'win':
            message = '🎉 KAMU MENANG! 🎉';
            detail = `${choices[playerChoice].name} mengalahkan ${choices[computerChoice].name}`;
            resultMessage.classList.add('win');
            break;
        case 'lose':
            message = '😢 KAMU KALAH 😢';
            detail = `${choices[computerChoice].name} mengalahkan ${choices[playerChoice].name}`;
            resultMessage.classList.add('lose');
            break;
        case 'draw':
            message = '🤝 SERI! 🤝';
            detail = `Kalian memilih ${choices[playerChoice].name} yang sama`;
            resultMessage.classList.add('draw');
            break;
    }

    resultMessage.textContent = message;
    resultDetail.textContent = detail;

    // Tambahkan animasi
    resultSection.style.animation = 'none';
    setTimeout(() => {
        resultSection.style.animation = 'slideIn 0.5s ease';
    }, 10);
}

// Fungsi untuk reset skor
function resetGame() {
    scores = {
        player: 0,
        computer: 0,
        draw: 0
    };

    document.getElementById('playerScore').textContent = '0';
    document.getElementById('computerScore').textContent = '0';
    document.getElementById('drawScore').textContent = '0';

    document.getElementById('playerChoice').innerHTML = `
        <div class="choice-emoji">?</div>
        <div class="choice-name">Menunggu...</div>
    `;

    document.getElementById('computerChoice').innerHTML = `
        <div class="choice-emoji">?</div>
        <div class="choice-name">Menunggu...</div>
    `;

    document.getElementById('resultMessage').textContent = 'Pilih salah satu pilihan untuk mulai!';
    document.getElementById('resultMessage').className = 'result-message';
    document.getElementById('resultDetail').textContent = '';

    document.querySelectorAll('.choice-btn').forEach(btn => {
        btn.classList.remove('active');
    });
}

// Tambahkan CSS animation secara dinamis
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);
