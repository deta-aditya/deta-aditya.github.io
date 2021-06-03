import React from 'react'
import './SectionHeading.css'

interface SectionHeadingProps {
  title: string
}

function SectionHeading(props: SectionHeadingProps) {
  return (
    <h1 className="section-heading">{props.title}</h1>
  )
}

export { SectionHeading }
