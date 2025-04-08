document.addEventListener("DOMContentLoaded", function () {
    const darkModeToggle = document.getElementById("dark-mode-toggle");
    const body = document.body;
  
    // Check for stored user preference
    if (localStorage.getItem("darkMode") === "enabled") {
      body.classList.add("dark-mode");
      darkModeToggle.textContent = "☀️ Light Mode";
    }
  
    // Toggle Dark Mode
    darkModeToggle.addEventListener("click", function () {
      body.classList.toggle("dark-mode");
  
      // Save preference in localStorage
      if (body.classList.contains("dark-mode")) {
        localStorage.setItem("darkMode", "enabled");
        // darkModeToggle.textContent = "☀️ Light Mode";
      } else {
        localStorage.setItem("darkMode", "disabled");
        // darkModeToggle.textContent = "🌙 Dark Mode";
      }
    });
  });
  