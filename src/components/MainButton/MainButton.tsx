import React, { PropsWithChildren } from 'react'
import './MainButton.css'

function MainButton(props: PropsWithChildren<{}>) {
  return (
    <button className="main-button">{props.children}</button>
  )
}

export { MainButton }