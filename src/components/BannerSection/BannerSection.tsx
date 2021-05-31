import React from 'react'
import './BannerSection.css'

function BannerSection() {
  return (
    <section className="banner-section">
      <p className="hello">Hello, I'm</p>
      <p className="name">
        <span className="nick-name">Deta</span>
        <span className="other-name"> Aditya</span>
      </p>
      <p className="profession">I'm a 
        <span className="typed-profession"> software developer_</span>
      </p>
      <button className="main-button">Hire Me</button>
    </section>
  )
}

export { BannerSection }