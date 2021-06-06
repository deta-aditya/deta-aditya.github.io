import React from 'react'
import { DateTime } from 'luxon'
import { TimelineView } from '../TimelineView'
import { SectionHeading } from '../SectionHeading'
import { useExperience } from "../../data/experience"
import './ExperienceSection.css'

function ExperienceSection() {
  const experience = useExperience()

  const dateFormat = (dateTime: DateTime): string =>
    dateTime.toFormat('yyyy LLL').toUpperCase()

  return (
    <section className="experience-section">
      <SectionHeading title="Experience" />
      <TimelineView>
        {experience.state === 'SUCCESS' && experience.data.map((experience, idx) => (
          <TimelineView.Item
            key={idx}
            range={`${dateFormat(experience.startDate)} - ${dateFormat(experience.endDate)}`}
            title={experience.position}
            subtitle={`${experience.employer} - ${experience.employment}`}
            tags={experience.tags}
          />
        ))}
      </TimelineView>
    </section>
  )
}

export { ExperienceSection }