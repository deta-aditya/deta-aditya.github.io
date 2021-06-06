import { ExperienceDataProvider, ExperienceJSON } from "./experience-types"

export const getFromLocalJSON: ExperienceDataProvider = () => {
  const experiences: ExperienceJSON[] = [
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

  return Promise.resolve(experiences)
}