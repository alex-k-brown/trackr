'use strict';

angular.module('myApp.achievements', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/achievements', {
            templateUrl: 'achievements/achievements.html',
            controller: 'achievementsCtrl'
        });
    }])

    .controller('achievementsCtrl', [function () {

    }]);