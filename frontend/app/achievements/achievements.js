'use strict';

angular.module('myApp.achievements', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/achievements', {
            templateUrl: 'achievements/achievements.html',
            controller: 'achievementsCtrl'
        });
    }])

    .controller('achievementsCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {


        Restangular.all('goals').getList().then(function(goals){
            $scope.goals = goals;

        });

    }]);