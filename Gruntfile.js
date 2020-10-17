const sass = require('node-sass');

module.exports = function (grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    sass: {
      options: {
        implementation: sass,
        sourceMap: false
      },
      styles: {
        files: {
          'static_global/main/gen/styles.css': 'apps/main/static/main/scss/styles.scss',
          'static_global/main/gen/1200.css': 'apps/main/static/main/scss/media/1200.scss',
          'static_global/main/gen/1140.css': 'apps/main/static/main/scss/media/1140.scss',
          'static_global/main/gen/992.css': 'apps/main/static/main/scss/media/992.scss',
          'static_global/main/gen/768.css': 'apps/main/static/main/scss/media/768.scss',
          'static_global/main/gen/576.css': 'apps/main/static/main/scss/media/576.scss',
          'static_global/main/gen/custom.css': 'apps/main/static/main/scss/media/custom.scss',
          'static_global/main/gen/not-minimize.css': 'apps/main/static/main/scss/not-minimize.scss',
          'static_global/main/gen/final.css': 'apps/main/static/main/scss/final.scss',
          'static_global/main/gen/sign.css': 'apps/main/static/main/scss/sign.scss',
          'static_global/main/gen/contact-us.css': 'apps/main/static/main/scss/contact-us.scss',
          'static_global/main/gen/comment.css': 'apps/main/static/main/scss/comment.scss',
          'static_global/main/gen/dropzone.css': 'apps/main/static/main/scss/dropzone.scss',
          'static_global/main/gen/404.css': 'apps/main/static/main/scss/404.scss',
          'static_global/main/gen/502.css': 'apps/main/static/main/scss/502.scss',
          'static_global/main/gen/spinner.css': 'apps/main/static/main/scss/spinner.scss',
          'static_global/main/gen/profile.css': 'apps/main/static/main/scss/profile.scss',
          'static_global/main/gen/subscription-plans.css': 'apps/main/static/main/scss/subscription-plans.scss',
        }
      },
    },
    babel: {
      options: {
        sourceMap: false,
        presets: ['@babel/preset-env'],
        compact: false
      },
      dist: {
        files: {
           'static_global/main/gen/js/scripts.compiled.js': 'apps/main/static/main/js/scripts.js',
           'static_global/main/gen/js/extra_locations.compiled.js': 'apps/main/static/main/js/extra_phones.js',
           'static_global/main/gen/js/extra_phones.compiled.js': 'apps/main/static/main/js/extra_locations.js',
           'static_global/main/gen/js/main.compiled.js':'apps/main/static/main/js/main.js',
        }
      }
    },
    concat: {
      company_extra_field_js:{
        src: [
          'static_global/main/gen/js/extra_locations.compiled.js',
          'static_global/main/gen/js/extra_phones.compiled.js',
        ],
        dest: 'static_global/main/gen/js/extra_fields.min.js'
      },
      covid_js: {
        src: [
          'apps/coronavirus/static/coronavirus/js/core.js',
          'apps/coronavirus/static/coronavirus/js/maps.js',
          'apps/coronavirus/static/coronavirus/js/charts.js',
          'apps/coronavirus/static/coronavirus/js/ukraineLow.js',
          'apps/coronavirus/static/coronavirus/js/js_map.js',
        ],
        dest: 'static_global/coronavirus/gen/covid.min.js'
      },
      js: {
        src: [
          'apps/main/static/django_js_reverse/js/reverse.js',
          'apps/main/static/main/libs/overlayscrollbars/overlayscrollbars.min.js',
          'node_modules/notyf/notyf.min.js',
          'node_modules/jquery/dist/jquery.min.js',
          'node_modules/lodash/lodash.min.js',
          'node_modules/jssocials/dist/jssocials.min.js',
          'node_modules/bootstrap/dist/js/bootstrap.min.js',
          'node_modules/@fancyapps/fancybox/dist/jquery.fancybox.min.js',
          'node_modules/js-cookie/src/js.cookie.js',
          'node_modules/file-upload-with-preview/dist/file-upload-with-preview.min.js',
          'node_modules/tabbyjs/dist/js/tabby.min.js',
          'node_modules/overlayscrollbars/js/OverlayScrollbars.js',

          'static_global/main/gen/js/scripts.compiled.js',
          'static_global/main/gen/js/main.compiled.js',
        ],
        dest: 'static_global/main/gen/all.js'
      },
      css: {
        src: [
          'node_modules/bootstrap/dist/css/bootstrap.min.css',
          'node_modules/@fancyapps/fancybox/dist/jquery.fancybox.css',
          'node_modules/file-upload-with-preview/dist/file-upload-with-preview.min.css',
          'node_modules/jssocials/dist/jssocials.css',
          'node_modules/jssocials/dist/jssocials-theme-flat.css',
          'node_modules/tabbyjs/dist/css/tabby-ui.min.css',
          'node_modules/notyf/notyf.min.css',
          'node_modules/overlayscrollbars/css/OverlayScrollbars.min.css',

          'apps/main/static/main/libs/slimselect/slimselect.min.css',
          'apps/main/static/main/libs/overlayscrollbars/overlayscrollbars.min.css',

          'static_global/main/gen/styles.css',
          'static_global/main/gen/1200.css',
          'static_global/main/gen/1140.css',
          'static_global/main/gen/992.css',
          'static_global/main/gen/768.css',
          'static_global/main/gen/576.css',
          'static_global/main/gen/custom.css',
          'static_global/main/gen/not-minimize.css',
          'static_global/main/gen/final.css',
          'static_global/main/gen/contact-us.css',
          'static_global/main/gen/comment.css',
          'static_global/main/gen/spinner.css',
          'static_global/main/gen/profile.css',
          'static_global/main/gen/subscription-plans.css',
        ],
        dest: 'static_global/main/gen/all.css'
      },
      auth: {
        src:[
          'static_global/main/gen/sign.css'
        ],
        dest: 'static_global/main/gen/auth.css'
      },
//      errorPages: {
//        src: [
//          'static_global/main/gen/502.css',
//          'static_global/main/gen/404.css',
//        ],
//        dest: 'static_global/main/gen/error-pages.css'
//      }
    },
    cssmin: {
      options: {
        root: './'
      },
      target: {
        files: [
          {
            expand: true,
            src: 'static_global/main/gen/all.css',
            ext: '.min.css'
          },
          {
            expand: true,
            src: 'static_global/main/gen/auth.css',
            ext: '.min.css'
          },
//          {
//            expand: true,
//            src: 'static_global/main/gen/error-pages.css'
//            ext: '.min.css'
//          }
        ]
      }
    },
    stripCssComments: {
        options: {
          preserve: false,
        },
        dist: {
            files: {
                'static_global/main/gen/all.min.css': 'static_global/main/gen/all.min.css',
                'static_global/main/gen/auth.min.css': 'static_global/main/gen/auth.min.css',
            }
        }
    },
    uglify: {
      js: {
        options: {
          sourceMap: false,
        },
        src: 'static_global/main/gen/all.js',
        dest: 'static_global/main/gen/all.min.js',
      }
    },
    watch: {
      options: {
        livereload: true
      },
      main: {
        files: [
          'apps/main/static/main/scss/**',
          'apps/main/static/main/js/**',
          'apps/main/static/main/angularJS/**'
        ],
        tasks: ['build']
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-babel');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  require('load-grunt-tasks')(grunt);
  require('grunt-contrib-concat')(grunt);

  grunt.registerTask(
    'build', [
      'sass:styles',
      'babel',
      'concat:js',
      'concat:covid_js',
      'concat:css',
      'concat:auth',
      'concat:company_extra_field_js',
      'cssmin',
      'stripCssComments',
      'uglify',
    ]);
  grunt.registerTask(
    'watch', [
      'sass:styles',
      'babel',
      'concat:js',
      'concat:covid_js',
      'concat:company_extra_field_js',
      'concat:css',
      'concat:auth',
      // 'cssmin',
      // 'stripCssComments',
      // 'uglify',
    ]
  );
};
