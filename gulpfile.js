var coffee = require('gulp-coffee'),
    gulp = require('gulp'),
    gutil = require('gulp-util'),
    sass = require('gulp-sass');

gulp.task('coffee', function() {
  gulp.src('static/coffee/**/*.coffee')
      .pipe(coffee({bare: true}).on('error', gutil.log))
      .pipe(gulp.dest('static/js/'));
});

gulp.task('foundation', function () {
  gulp.src('static/scss/**/*.scss')
      .pipe(sass())
      .pipe(gulp.dest('static/css'));
});

gulp.task('default', function() {
  gulp.run('coffee');
  gulp.run('foundation');

  gulp.watch('static/coffee/**/*', function() {
    gulp.run('coffee');
  });

  gulp.watch('static/scss/**/*.scss', function() {
    gulp.run('foundation');
  });
});
