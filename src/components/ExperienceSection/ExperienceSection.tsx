import React from 'react'
import './ExperienceSection.css'

function ExperienceSection() {
  return (
    <section className="experience-section">
      <h1 className="section-heading">Experience</h1>
      <div className="timeline">
        <article className="timeline-item">
          <div className="timeline-line"></div>
          <div className="timeline-dot"></div>
          <p className="timeline-range">2020 NOV - 2021 APR</p>
          <main className="timeline-main">
            <h2 className="title">IT Technical Manager</h2>
            <p className="subtitle">LiveIn - Full Time</p>
            <div className="timeline-tags">
              <span className="tag-item">Project Management</span>
              <span className="tag-item">Software Architecture</span>
              <span className="tag-item">Test Driven Development</span>
              <span className="tag-item">Go</span>
              <span className="tag-item">Laravel</span>
              <span className="tag-item">iOS</span>
            </div>
          </main>
        </article>
      </div>
    </section>
  )
}

export { ExperienceSection }