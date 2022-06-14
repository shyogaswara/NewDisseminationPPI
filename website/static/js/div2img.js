function takeimage() {
    html2canvas(document.querySelector("#capture"), {
        allowTaint: true,
        useCORS: true,
    }).then(canvas => {
        var link = document.createElement("a");
        document.body.appendChild(link);
        link.download = "event.jpg";
        link.href = canvas.toDataURL();
        link.target = '_blank';
        link.click();
    });
}