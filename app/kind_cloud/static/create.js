const codeOfConduct = document.getElementById('conduct')
const readCode = localStorage.getItem('code-of-conduct')
if (!readCode) {
    codeOfConduct.showModal()
    codeOfConduct.addEventListener('close', () => {
        localStorage.setItem('code-of-conduct', 'true')
    })
}
