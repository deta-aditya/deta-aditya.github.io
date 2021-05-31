import React from 'react'
import './BannerSection.css'
import { MainButton } from '../MainButton'

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
      <div className="button-placeholder">
        <MainButton>Hire Me</MainButton>
      </div>
    </section>
  )
}

export { BannerSection }