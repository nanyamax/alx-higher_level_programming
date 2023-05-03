function toggleHeader() {
  const header = $("header");
  if (header.attr("class") === "green") {
    header.attr("class", "red");
  } else {
    header.attr("class", "green");
  }
}
