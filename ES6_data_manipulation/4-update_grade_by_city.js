export default function updateStudentGradeByCity(data, city, newGrades) {
  const dataStudent = data.filter((data) => data.location === city);
  const dataUpdateStudent = dataStudent.map((data) => {
    const gradeEntry = newGrades.find((grade) => grade.dataId === data.id);
    return {
      ...data,
      grade: gradeEntry ? gradeEntry.grade : 'N/A',
    };
  });
  return dataUpdateStudent;
}
