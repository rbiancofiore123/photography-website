/**
 * Photography Portfolio - Main JavaScript
 * Handles navigation, smooth scrolling, and active link highlighting
 */

'use strict';

// =============================================================================
// Constants
// =============================================================================

const SELECTORS = {
    navLink: '.nav-link',
    sections: 'main section[id]',
    currentYear: '#current-year',
};

const OBSERVER_OPTIONS = {
    rootMargin: '-40% 0px -50% 0px',
    threshold: 0.1,
};

const SCROLL_OFFSET = 120;

// =============================================================================
// DOM Element References
// =============================================================================

const navLinks = document.querySelectorAll(SELECTORS.navLink);
const sections = document.querySelectorAll(SELECTORS.sections);
const yearElement = document.querySelector(SELECTORS.currentYear);

// =============================================================================
// Navigation Functions
// =============================================================================

/**
 * Updates the active state of navigation links
 * @param {string} activeId - The ID of the currently active section
 */
function updateActiveLink(activeId) {
    if (!activeId) return;

    navLinks.forEach((link) => {
        const href = link.getAttribute('href');
        const isActive = href === `#${activeId}`;
        
        link.classList.toggle('active', isActive);
        
        if (isActive) {
            link.setAttribute('aria-current', 'page');
        } else {
            link.removeAttribute('aria-current');
        }
    });
}

/**
 * Handles smooth scrolling for anchor links
 * @param {Event} event - Click event
 */
function handleSmoothScroll(event) {
    const link = event.currentTarget;
    const href = link.getAttribute('href');
    
    if (!href || !href.startsWith('#')) {
        return;
    }

    const target = document.querySelector(href);
    
    if (!target) {
        console.warn(`Target element ${href} not found`);
        return;
    }

    event.preventDefault();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// =============================================================================
// Intersection Observer (Modern Browsers)
// =============================================================================

/**
 * Initializes Intersection Observer for active link tracking
 */
function initIntersectionObserver() {
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    updateActiveLink(entry.target.id);
                }
            });
        },
        OBSERVER_OPTIONS
    );

    sections.forEach((section) => observer.observe(section));
}

// =============================================================================
// Fallback Scroll Handler (Legacy Browsers)
// =============================================================================

/**
 * Fallback active link tracking using scroll events
 */
function initScrollHandler() {
    function setActiveLink() {
        const fromTop = window.scrollY + SCROLL_OFFSET;
        
        sections.forEach((section) => {
            const top = section.offsetTop;
            const bottom = top + section.offsetHeight;
            
            if (fromTop >= top && fromTop < bottom) {
                updateActiveLink(section.id);
            }
        });
    }

    setActiveLink();
    window.addEventListener('scroll', setActiveLink, { passive: true });
}

// =============================================================================
// Utility Functions
// =============================================================================

/**
 * Sets the current year in the footer
 */
function setCurrentYear() {
    if (!yearElement) {
        console.warn('Current year element not found');
        return;
    }
    
    const currentYear = new Date().getFullYear();
    yearElement.textContent = currentYear;
}

// =============================================================================
// Initialization
// =============================================================================

/**
 * Initializes all functionality
 */
function init() {
    // Set up smooth scrolling
    navLinks.forEach((link) => {
        link.addEventListener('click', handleSmoothScroll);
    });

    // Set up active link tracking
    if ('IntersectionObserver' in window && sections.length > 0) {
        initIntersectionObserver();
    } else if (sections.length > 0) {
        initScrollHandler();
    }

    // Set current year
    setCurrentYear();
}

// Start the application
init();
