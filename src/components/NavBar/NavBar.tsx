import React from 'react'
import './NavBar.css'

function NavBar() {
  return (
    <nav className="nav-bar">
      <a href="/experience" className="nav-item">Experience</a>
      <a href="/education" className="nav-item">Education</a>
      <a href="/accomps" className="nav-item">Accomplishments</a>
      <a href="/skills" className="nav-item">Skills</a>
      <a href="/contact" className="nav-item">Contact</a>
    </nav>
  )
}

export { NavBar }