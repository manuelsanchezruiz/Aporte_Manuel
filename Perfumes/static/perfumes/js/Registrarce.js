document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.getElementById('id_password1');
    const strengthBar = document.getElementById('password-strength-bar');

    passwordInput.addEventListener('input', function() {
        const value = passwordInput.value;
        const strength = calculatePasswordStrength(value);

        strengthBar.style.width = strength.percent + '%';
        strengthBar.setAttribute('aria-valuenow', strength.percent);
        strengthBar.className = 'progress-bar ' + strength.color;
        strengthBar.textContent = strength.text;
    });

    function calculatePasswordStrength(password) {
        let score = 0;

        if (password.length >= 8) score++;
        if (password.length >= 12) score++;
        if (/[A-Z]/.test(password)) score++;
        if (/[a-z]/.test(password)) score++;
        if (/\d/.test(password)) score++;
        if (/[!@#$%^&*()_+=-]/.test(password)) score++;

        let percent = (score / 6) * 100;
        let color = '';
        let text = '';

        if (score <= 2) {
            color = 'bg-danger';
            text = 'Insegura';
        } else if (score <= 4) {
            color = 'bg-warning';
            text = 'Segura';
        } else {
            color = 'bg-success';
            text = 'Muy segura';
        }

        return { percent: percent, color: color, text: text };
    }
});
