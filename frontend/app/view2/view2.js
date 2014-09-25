'use strict';

angular.module('myApp.view2', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view2', {
    templateUrl: 'view2/view2.html',
    controller: 'View2Ctrl'
  });
}])

.controller('View2Ctrl', ['Restangular', function(Restangular) {
        // GET a list of all goals
        Restangular.all('goals').getList().then(function (goals) {
            $scope.goals = goals;
        });
    }])
