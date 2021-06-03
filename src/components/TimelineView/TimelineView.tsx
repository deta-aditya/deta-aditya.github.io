import React, { createContext, useContext, PropsWithChildren } from 'react'
import './TimelineView.css'

const Context = createContext(null)

function TimelineView(props: PropsWithChildren<{}>) {
  return (
    <Context.Provider value={null}>
      <div className="timeline">
        {props.children}
      </div>
    </Context.Provider>
  )
}

interface TimelineViewItemProps {
  range: string
  title: string
  subtitle: string
  tags?: string[]
  children?: never
}

function Item(props: TimelineViewItemProps) {
  const context = useContext(Context)

  if (context === undefined) {
    throw new Error("TimelineView.Item can't be rendered outside TimelineView")
  }
  
  return (
    <article className="timeline-item">
      <div className="timeline-line"></div>
      <div className="timeline-dot"></div>
      <p className="timeline-range">{props.range}</p>
      <main className="timeline-main">
        <h2 className="title">{props.title}</h2>
        <p className="subtitle">{props.subtitle}</p>
        {props.tags && (
          <div className="timeline-tags">
            {props.tags.map(tag => (
              <span key={tag} className="tag-item">{tag}</span>
            ))}
          </div>
        )}
      </main>
    </article>
  )
}

TimelineView.Item = Item

export { TimelineView }
