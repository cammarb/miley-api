function openTracklist() {
    const tracklist = document.querySelector(".tracklist");

    tracklist.classList.add("open");

}

function closeTracklist() {
    const tracklist = document.querySelector(".tracklist");

    if (tracklist.classList.contains("open")) {
        tracklist.classList.remove("open");
    }
}