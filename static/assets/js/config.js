"use strict";
(window.config = {
    colors: {
        primary: "#7367f0",
        secondary: "#808390",
        success: "#28c76f",
        info: "#00bad1",
        warning: "#ff9f43",
        danger: "#FF4C51",
        dark: "#4b4b4b",
        black: "#000",
        white: "#fff",
        cardColor: "#fff",
        bodyBg: "#f8f7fa",
        bodyColor: "#6d6b77",
        headingColor: "#444050",
        textMuted: "#acaab1",
        borderColor: "#e6e6e8",
    },
    colors_label: { primary: "#7367f029", secondary: "#a8aaae29", success: "#28c76f29", info: "#00cfe829", warning: "#ff9f4329", danger: "#ea545529", dark: "#4b4b4b29" },
    colors_dark: { cardColor: "#2f3349", bodyBg: "#25293c", bodyColor: "#b2b1cb", headingColor: "#cfcce4", textMuted: "#8285a0", borderColor: "#565b79" },
    enableMenuLocalStorage: !0,
}),
    (window.assetsPath = document.documentElement.getAttribute("data-assets-path")),
    (window.templateName = document.documentElement.getAttribute("data-template")),
    (window.rtlSupport = !0),
    "undefined" != typeof TemplateCustomizer &&
        (window.templateCustomizer = new TemplateCustomizer({
            cssPath: assetsPath + "vendor/css" + (rtlSupport ? "/rtl" : "") + "/",
            themesPath: assetsPath + "vendor/css" + (rtlSupport ? "/rtl" : "") + "/",
            displayCustomizer: !0,
            lang: localStorage.getItem("templateCustomizer-" + templateName + "--Lang") || "en",
            controls: ["rtl", "style", "headerType", "contentLayout", "layoutCollapsed", "layoutNavbarOptions", "themes"],
        }));
