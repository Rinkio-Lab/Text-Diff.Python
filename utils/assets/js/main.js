function runDiff() {
    const text1 = document.getElementById('text1').value.trim();
    const text2 = document.getElementById('text2').value.trim();
    const messageDiv = document.getElementById('message');
    const diffType = document.getElementById('diffType').value;

    if (!text1 || !text2) {
        showMessage('请输入需要对比的文本', 'warning');
        return;
    }

    const diff = Diff[diffType](text1, text2);
    const resultDiv = document.getElementById('diffResult');
    // show
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = '';

    diff.forEach(part => {
        const span = document.createElement('span');
        span.textContent = part.value;
        if (part.added) span.className = 'added';
        else if (part.removed) span.className = 'removed';
        resultDiv.appendChild(span);
    });
}

function showMessage(text, type = 'info') {
    const msg = document.getElementById('message');
    msg.textContent = text;
    msg.className = `message ${type}`;
    msg.style.opacity = 1;
    setTimeout(() => (msg.style.opacity = 0), 3000);
}

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('runDiffBtn').addEventListener('click', runDiff);
});
