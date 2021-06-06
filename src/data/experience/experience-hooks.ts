import { useEffect, useState } from "react"
import { getFromLocalJSON } from "./experience-data-providers"
import { fromJSON } from "./experience-factories"
import { ExperienceDataProvider, ExperienceState } from "./experience-types"

export function useExperience() {
  const dataProvider: ExperienceDataProvider = getFromLocalJSON
  
  const [experience, setExperience] = useState<ExperienceState>({ state: 'INITIAL' })

  useEffect(() => {
    setExperience({ state: 'LOADING' })

    dataProvider().then(data => {
      const experiences = data.map(fromJSON)
      setExperience({ state: 'SUCCESS', data: experiences })
    })

  }, [dataProvider, setExperience])

  return experience
}