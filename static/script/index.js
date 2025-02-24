(async() => {
    const inputEmulator = document.getElementById('inputEmulator');
    const inputRom = document.getElementById('inputRom');
    const button = document.querySelector('button');
    button.disabled = true;
    inputEmulator.addEventListener('change', async (event) => {
        const response = await fetch(`/roms?console=${event.target.value}`);
        const data = await response.json();
        inputRom.innerHTML = '<option selected disabled>Escolha um game...</option>';
        data.forEach(rom => {
            const option = document.createElement('option');
            option.value = rom.name;
            option.textContent = rom.name;
            inputRom.appendChild(option);
        });
        button.disabled = false;
    });
})();