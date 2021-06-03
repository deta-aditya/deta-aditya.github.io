import React from 'react'
import { TimelineView } from '../TimelineView'
import { SectionHeading } from '../SectionHeading'
import './ExperienceSection.css'
import { DateTime } from 'luxon'

interface ExperienceJson {
  position: string
  employer: string
  employment: string
  start_date: string
  end_date: string
  tags: string[]
}

function ExperienceSection() {
  const experiences: ExperienceJson[] = [
    {
      position: "IT Technical Manager",
      employer: "LiveIn",
      employment: "Full Time",
      start_date: "2020-11-09T00:00:00.000Z",
      end_date: "2021-04-12T00:00:00.000Z",
      tags: [
        "Project Management",
        "Software Architecture",
        "Test Driven Development",
        "Go",
        "Laravel",
        "iOS",
      ],
    },
    {
      position: "Frontend Developer",
      employer: "ProcurA",
      employment: "Full Time",
      start_date: "2019-07-08T00:00:00.000Z",
      end_date: "2020-12-28T00:00:00.000Z",
      tags: [
        "Angular.js",
        "CoffeeScript",
        "React",
        "TypeScript",
      ],
    }
  ]

  const dateFormat = (dateString: string): string =>
    DateTime.fromISO(dateString).toFormat('yyyy LLL').toUpperCase()

  return (
    <section className="experience-section">
      <SectionHeading title="Experience" />
      <TimelineView>
        {experiences.map((experience, idx) => (
          <TimelineView.Item
            key={idx}
            range={`${dateFormat(experience.start_date)} - ${dateFormat(experience.end_date)}`}
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