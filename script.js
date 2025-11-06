/**
 * Toggles the display of an individual team member's bio
 * @param {string} bioId - The ID of the bio section to show or hide
 * @param {string} moodboardId - The ID of the moodboard container (optional)
 */
function toggleBio(bioId, moodboardId = null) {
    const bio = document.getElementById(bioId);
    // Toggle between showing and hiding the bio section
    if (bio.style.display === "none" || bio.style.display === "") {
        bio.style.display = "block";

        // If moodboard ID is provided, show the moodboard as well
        if (moodboardId) {
            const moodboard = document.getElementById(moodboardId);
            moodboard.style.display = "block";
        }
    } else {
        bio.style.display = "none";

        // If moodboard ID is provided, hide the moodboard as well
        if (moodboardId) {
            const moodboard = document.getElementById(moodboardId);
            moodboard.style.display = "none";
        }
    }
}

/**
 * Shows the specified section ('bios' or 'vision') and hides the other
 * @param {string} sectionId - The ID of the section to display
 */
function showSection(sectionId) {
    const biosSection = document.getElementById("bios");
    const visionSection = document.getElementById("vision");

    // Display the bios section and hide the vision section
    if (sectionId === "bios") {
        biosSection.style.display = "flex";
        visionSection.style.display = "none";
    }
    // Display the vision section and hide the bios section
    else if (sectionId === "vision") {
        biosSection.style.display = "none";
        visionSection.style.display = "block";
    }
}