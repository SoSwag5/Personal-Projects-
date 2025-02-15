document.getElementById('jobForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Job Posted Successfully!');
});

document.getElementById('cvForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    alert('CV Saved Successfully!');
});

function generateReport() {
    alert('Report Generated Successfully!');
}
