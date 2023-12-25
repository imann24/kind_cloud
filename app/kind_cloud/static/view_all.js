function zoomOnKindCloud(text) {
    const modal = document.getElementById('zoom')
    modal.getElementsByClassName('text-container')[0].innerHTML = text
    modal.showModal()
    modal.scrollTo(0, 0)
    // source: https://stackoverflow.com/a/26984690/5204093
    modal.addEventListener('click', function(event) {
        const rect = modal.getBoundingClientRect()
        const isInDialog = (rect.top <= event.clientY && event.clientY <= rect.top + rect.height &&
          rect.left <= event.clientX && event.clientX <= rect.left + rect.width)
        if (!isInDialog) {
            modal.close()
        }
    })
}
