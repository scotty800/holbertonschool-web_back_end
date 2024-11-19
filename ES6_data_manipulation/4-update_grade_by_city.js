export default function updateStudentGradeByCity(data, city, newGrades) {
  const dataStudent = data.filter((student) => student.location === city);
  const dataUpdateStudent = dataStudent.map((student) => {
    const gradeEntry = newGrades.find((grade) => grade.studentId === student.id);
    return {
      ...student,
      grade: gradeEntry ? gradeEntry.grade : 'N/A',
    };
  });

  return dataUpdateStudent;
}
