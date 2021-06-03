import React from 'react'
import { TimelineView } from '../TimelineView'
import './ExperienceSection.css'

function ExperienceSection() {
  return (
    <section className="experience-section">
      <h1 className="section-heading">Experience</h1>
      <TimelineView>
        <TimelineView.Item 
          range="2020 NOV - 2021 APR"
          title="IT Technical Manager"
          subtitle="LiveIn - Full Time"
          tags={[
            "Project Management",
            "Software Architecture",
            "Test Driven Development",
            "Go",
            "Laravel",
            "iOS",
          ]}
        /> 
      </TimelineView>
    </section>
  )
}

export { ExperienceSection }