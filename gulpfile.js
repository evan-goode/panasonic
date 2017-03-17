const gulp = require('gulp');

const gulpUtil = require('gulp-util');
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');
const pug = require('gulp-pug');
const babel = require('gulp-babel');
const notify = require('gulp-notify');

const paths = {
  sass: ['**/*.sass', '**/*.scss', '!node_modules/**'],
  pug: ['**/*.jade', '**/*.pug', '!node_modules/**'],
  babel: ['**/*.babel', '!node_modules/**']
};

function errorHandler (error) {
  gulpUtil.log(gulpUtil.colors.red(error.message));
  this.emit('end');
}

gulp.task('default', ['sass', 'pug', 'babel']);

gulp.task('sass', () => {
  return gulp.src(paths.sass)
    .pipe(sass())
    .on('error', errorHandler)
    .pipe(autoprefixer())
    .on('error', errorHandler)
    .pipe(gulp.dest('.'))
		.pipe(notify("<%= file.relative %>"));
});

gulp.task('pug', () => {
  return gulp.src(paths.pug)
    .pipe(pug())
    .on('error', errorHandler)
    .pipe(gulp.dest('.'))
		.pipe(notify("<%= file.relative %>"));
});

gulp.task('babel', () => {
  return gulp.src(paths.babel)
    .pipe(babel({
      presets: ['es2015']
    }))
    .on('error', errorHandler)
    .pipe(gulp.dest('.'))
		.pipe(notify("<%= file.relative %>"));
});

gulp.task('watch', () => {
  gulp.watch(paths.sass, ['sass']);
  gulp.watch(paths.pug, ['pug']);
  gulp.watch(paths.babel, ['babel']);
});
