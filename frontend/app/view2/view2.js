'use strict';

angular.module('myApp.view2', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/view2', {
            templateUrl: 'view2/view2.html',
            controller: 'View2Ctrl'
        })
    }])

    .controller('View2Ctrl', ['Restangular', function (Restangular) {
        // GET a list of all goals
        Restangular.all('goals').getList().then(function (goals) {
            $scope.goals = goals;
        })
    }])

    .controller('View2Ctrl', ['Restangular', '$scope', function (Restangular, $scope) {
        // GET a list of all timeFrames
        Restangular.all('goals').getList().then(function (timeFrames) {
            $scope.timeFrames = timeFrames;
        })


            $scope.today = function () {
                $scope.dt = new Date();
            };
            $scope.today();
            0
            $scope.clear = function () {
                $scope.dt = null;
            };
            $scope.toggleMin = function () {
                $scope.minDate = $scope.minDate ? null : new Date();
            };
            $scope.toggleMin();

            $scope.open = function ($event) {
                $event.preventDefault();
                $event.stopPropagation();

                $scope.opened = true;
            };

            $scope.dateOptions = {
                formatYear: 'yy',
                startingDay: 1
            };

            $scope.initDate = new Date('2016-15-20');
            $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
            $scope.format = $scope.formats[0];

    }])

    .controller('EditGoalCtrl', function ($scope, Restangular, $routeParams, $location) {
        $scope.goalId = $routeParams.goalId;
        Restangular.one('goals', $scope.goalId).customGET().then(function (data) {
            $scope.goal = data;
        });
        $scope.updateGoal = function () {
            Restangular.one('goals', $scope.goalId).customPUT($scope.goal).then(function (data) {
                    $scope.status = "The recipe was successfully edited!";
                    $scope.goal = data;
                    $location.path('/goals');
                }, function () {
                    $scope.status = "The goal couldn't be saved";
                }
            )

        };
        $scope.deleteGoal = function () {
            if (confirm("Are you sure you want to delete this goal?")) {
                Restangular.one('goals', $scope.goalId).customDELETE().then(function (data) {
                    $location.path('/goals');
                }, function () {
                    $scope.status = "The goal couldn't be deleted";
                });
            }

        };
    });