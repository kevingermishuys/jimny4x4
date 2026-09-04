/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

/**
 * Touch/scroll photo carousel used by the fleet gallery snippet
 * (s_jimny_fleet_gallery). Builds the dot indicators, wires the
 * prev/next buttons and keeps the active dot in sync while scrolling.
 */
publicWidget.registry.JimnyGallery = publicWidget.Widget.extend({
    selector: ".s_jimny_gallery",

    start() {
        const track = this.el.querySelector(".gallery-track");
        const dotsWrap = this.el.querySelector(".gallery-dots");
        if (!track || !dotsWrap || dotsWrap.children.length) {
            return this._super(...arguments);
        }

        const slides = track.querySelectorAll(".gallery-slide");
        slides.forEach((_, i) => {
            const dot = document.createElement("button");
            dot.type = "button";
            dot.setAttribute("aria-label", "Go to photo " + (i + 1));
            if (i === 0) {
                dot.classList.add("active");
            }
            dot.addEventListener("click", () => {
                track.scrollTo({ left: track.clientWidth * i, behavior: "smooth" });
            });
            dotsWrap.appendChild(dot);
        });

        const dots = dotsWrap.querySelectorAll("button");
        const updateActive = () => {
            const idx = Math.round(track.scrollLeft / track.clientWidth);
            dots.forEach((d, i) => d.classList.toggle("active", i === idx));
        };
        track.addEventListener("scroll", () => window.requestAnimationFrame(updateActive), { passive: true });

        const prevBtn = this.el.querySelector(".gallery-nav.prev");
        const nextBtn = this.el.querySelector(".gallery-nav.next");
        if (prevBtn) {
            prevBtn.addEventListener("click", () => {
                track.scrollTo({ left: track.scrollLeft - track.clientWidth, behavior: "smooth" });
            });
        }
        if (nextBtn) {
            nextBtn.addEventListener("click", () => {
                track.scrollTo({ left: track.scrollLeft + track.clientWidth, behavior: "smooth" });
            });
        }

        return this._super(...arguments);
    },
});

/**
 * "All / Explorer / Overlander / Special Vehicle" filter pills on the
 * full fleet grid snippet (s_jimny_fleet_gallery).
 */
publicWidget.registry.JimnyFleetFilter = publicWidget.Widget.extend({
    selector: ".s_jimny_fleet_gallery .filter-row",

    events: {
        "click .filter-pill": "_onFilterClick",
    },

    _onFilterClick(ev) {
        const btn = ev.currentTarget;
        const grid = this.el.closest(".s_jimny_fleet_gallery").querySelector(".fleet-grid");
        this.el.querySelectorAll(".filter-pill").forEach((p) => p.classList.remove("active"));
        btn.classList.add("active");
        const filter = btn.getAttribute("data-filter");
        grid.querySelectorAll(".ticket").forEach((t) => {
            const show = filter === "all" || t.getAttribute("data-category") === filter;
            t.style.display = show ? "" : "none";
        });
    },
});

export default {
    JimnyGallery: publicWidget.registry.JimnyGallery,
    JimnyFleetFilter: publicWidget.registry.JimnyFleetFilter,
};
